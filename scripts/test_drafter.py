#!/usr/bin/env python3
"""Regression tests for scripts/draft_claims.py and scripts/fetch_evidence.py.

Every fixture in scripts/fixtures/epmc/ is a real Europe PMC record that once
produced a wrong claim on a live page. Run: python3 -m unittest scripts/test_drafter.py
"""
from __future__ import annotations

import json
import pathlib
import sys
import unittest

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import draft_claims as dc  # noqa: E402
import fetch_evidence as fe  # noqa: E402

FIX = HERE / "fixtures" / "epmc"


def paper(pmid: str) -> dict:
    return json.loads((FIX / f"{pmid}.json").read_text(encoding="utf-8"))


class SampleSize(unittest.TestCase):
    def test_space_separated_thousands(self):
        # BMJ Medicine 2026 network meta-analysis: read as n=214 on two live pages.
        self.assertEqual(dc.sample_size("58 trials of 24 214 participants were analysed."), 24214)

    def test_comma_separated_thousands(self):
        self.assertEqual(dc.sample_size("A total of 17,604 patients were enrolled"), 17604)
        self.assertEqual(dc.sample_size("Four RCTs encompassing 5425 participants were included."), 5425)

    def test_year_is_not_a_count(self):
        self.assertEqual(dc.sample_size("Between 2015 and 2019, 30 patients were treated."), 30)

    def test_enrolment_beats_subgroup_n(self):
        text = "The renal impairment study included 33 participants (normal function, n = 14; mild impairment, n = 7)."
        self.assertEqual(dc.sample_size(text), 33)


class Designs(unittest.TestCase):
    def test_network_meta_analysis_is_not_a_trial(self):
        p = paper("42688617")
        tier, _ = fe.classify(p)
        self.assertEqual(tier, "review")
        a = dc.analyse(p, ["retatrutide"], allow_synthesis=True)
        self.assertEqual(a["design"], "Network meta-analysis")
        self.assertEqual(a["n"], 24214)
        self.assertIsNone(dc.analyse(p, ["retatrutide"]), "a synthesis never becomes a compound-page claim")

    def test_meta_analysis_label(self):
        a = dc.analyse(paper("42583410"), ["cagrilintide", "CagriSema"], allow_synthesis=True)
        self.assertEqual(a["design"], "Meta-analysis")
        self.assertEqual(a["n"], 5425)

    def test_pharmacokinetic_study_sample_size(self):
        # Europe PMC tags this renal/hepatic impairment study as a randomised
        # trial, and that label wins; the live-page error was the number.
        a = dc.analyse(paper("42228334"), ["cagrilintide"])
        self.assertIn(a["design"], ("Randomized controlled trial", "Pharmacokinetic study"))
        self.assertNotEqual(a["n"], 14, "n=14 was a subgroup, not the study")

    def test_pharmacokinetic_label_from_title(self):
        p = {"pmid": "1", "title": "Pharmacokinetics of ipamorelin in healthy volunteers", "pubYear": "1999",
             "abstractText": "Twelve volunteers received ipamorelin 5 mg intravenously. Plasma half-life was 2 hours.", "pubTypeList": None, "meshHeadingList": None}
        self.assertEqual(dc.analyse(p, ["ipamorelin"])["design"], "Pharmacokinetic study")

    def test_imaging_label(self):
        a = dc.analyse(paper("32342318"), ["Selank", "Semax"])
        self.assertEqual(a["design"], "Imaging study")

    def test_randomised_trial_keeps_pubtype_label(self):
        a = dc.analyse(paper("37366315"), ["retatrutide"])
        self.assertIn("Randomized", a["design"])
        self.assertEqual(a["n"], 338)


class Mentions(unittest.TestCase):
    def test_hyphenated_identifiers_are_not_the_alias(self):
        self.assertFalse(fe.mentions("stepwise titration of 113Cd-MT-II with pHOHgBzO", ["MT-II"]))
        self.assertFalse(fe.mentions("the antagonist [D-Lys3]-GHRP-6 blocked the response", ["GHRP-6"]))

    def test_suffixes_and_real_uses_still_match(self):
        self.assertTrue(fe.mentions("MT-II (0.025 mg/kg) was administered subcutaneously", ["MT-II"]))
        self.assertTrue(fe.mentions("GHRP-6-induced GH secretion was blocked", ["GHRP-6"]))
        self.assertTrue(fe.mentions("semaglutide-treated participants lost weight", ["semaglutide"]))

    def test_mixed_case_homonym(self):
        self.assertFalse(fe.mentions("the SeMax increased by 2.9 mm (p = 0.0013)", ["Semax"]))
        self.assertTrue(fe.mentions("Administration of semax increased BDNF", ["Semax"]))
        self.assertTrue(fe.mentions("SEMAX IN ACUTE ISCHEMIC STROKE", ["Semax"]))


    def test_separator_and_amide_variants(self):
        names = ["Sermorelin", "GHRH(1-29)", "GHRH 1-29"]
        for text in ("a single dose of GHRH(1-29)NH2 was given", "priming with GHRH (1-29) NH2", "GHRH-(1-29)-NH2 infusion", "bolus GHRH 1-29 at 1 mcg/kg"):
            self.assertTrue(fe.mentions(text, names), text)
        self.assertTrue(fe.mentions("BPC157 infusion in humans", ["BPC-157"]))
        self.assertFalse(fe.mentions("GHRH antagonists suppress tumour growth", names))

    def test_roman_numeral_name_variants(self):
        names = ["Melanotan II", "Melanotan-II", "MT-II", "melanotan 2"]
        for text in ("Preformulation studies with melanotan-II", "synthesis of melanotan II",
                     "MELANOTAN II products sold online", "Melanotan II was administered subcutaneously"):
            self.assertTrue(fe.mentions(text, names), text)

    def test_unicode_dashes_in_names(self):
        for dash in ("-", "\u2010", "\u2011", "\u2013"):
            self.assertTrue(fe.mentions(f"MOTS{dash}c protects against placental injury", ["MOTS-c"]), dash)
        self.assertFalse(fe.mentions("R13A\u2011MOTS-c was delivered by LAT1", ["MOTS-c"]),
                         "an engineered analogue is not the parent compound")

    def test_coded_alias_needs_capitals(self):
        self.assertTrue(fe.mentions("KPV reduced intestinal inflammation", ["KPV"]))
        self.assertFalse(fe.mentions("the kpv gene cluster", ["KPV"]))


class MeasuredNotGiven(unittest.TestCase):
    def test_assay_paper_is_flagged(self):
        a = dc.analyse(paper("36490309"), ["MOTS-c"])
        self.assertIs(a["given"], False)
        self.assertTrue(a["design"].endswith("(MOTS-c measured, not given)"))
        self.assertEqual(a["doses"], [], "dose sentences in an assay paper describe other agents")

    def test_exercise_biomarker_paper_is_flagged(self):
        a = dc.analyse(paper("34413391"), ["MOTS-c"])
        self.assertIs(a["given"], False)

    def test_administered_trial_is_not_flagged(self):
        a = dc.analyse(paper("37366315"), ["retatrutide"])
        self.assertIs(a["given"], True)
        self.assertNotIn("measured, not given", a["design"])

    def test_animal_dosing_is_given(self):
        a = dc.analyse(paper("39212900"), ["Retatrutide"])
        self.assertIs(a["given"], True)


class SubjectMatch(unittest.TestCase):
    def test_exclusion_terms_reject_homonyms(self):
        entry = {"name": "Melanotan II", "aliases": ["MT-II"], "exclude_terms": ["metallothionein"]}
        p = {"title": "Cadmium binding to metallothionein-II", "abstractText": "MT-II binds cadmium. MT-II was titrated."}
        self.assertFalse(fe.subject_match(p, entry))

    def test_parent_sequence_citation_is_not_a_subject(self):
        entry = {"name": "Sermorelin", "aliases": ["GHRH(1-29)"]}
        p = {"title": "GHRH antagonist MIA-602 suppresses tumour growth", "abstractText": "The antagonist is derived from GHRH(1-29) by substitution. Tumours shrank."}
        self.assertFalse(fe.subject_match(p, entry))

    def test_single_mention_with_administration_is_kept(self):
        entry = {"name": "FOXO4-DRI", "aliases": []}
        p = {"title": "Cellular senescence contributes to bronchopulmonary dysplasia", "abstractText": "KYC, TUDCA, and FOXO4-DRI were administered intraperitoneally. Senescence fell."}
        self.assertTrue(fe.subject_match(p, entry))

    def test_title_mention_is_kept(self):
        self.assertTrue(fe.subject_match(paper("37366315"), {"name": "Retatrutide", "aliases": ["LY3437943"]}))


if __name__ == "__main__":
    unittest.main()
