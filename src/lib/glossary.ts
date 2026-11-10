// A-Z glossary of terms used on the record pages. Definitions are the site's
// own explanatory text (editorial, like the written guide sections): they
// explain vocabulary and make no claim about any compound's effects. Links go
// to the records where the term matters, never to a source it does not cite.
import { linker, type Target } from './entities';

export type Term = { term: string; id: string; def: string; see?: Array<[label: string, href: string]>; aka?: string };

const t = (term: string, def: string, see?: Term['see'], aka?: string): Term =>
  ({ term, id: term.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, ''), def, see, aka });

export const TERMS: Term[] = [
  t('Adverse event', 'Any unwanted medical event during a study, whether or not the compound caused it. Trials record them all and then judge which may be related. A list of adverse events is not a list of proven side effects.'),
  t('Agonist', 'A molecule that binds a receptor and switches it on, imitating the body\'s own signal. Many peptides on this site are named for the receptor they activate, for example a GLP-1 receptor agonist.'),
  t('Amylin analogue', 'A modified version of amylin, a hormone released with insulin that slows stomach emptying and signals fullness. Cagrilintide is a long-acting amylin analogue.', [['Cagrilintide', '/compounds/cagrilintide']]),
  t('Analogue', 'A molecule built to resemble a natural one, usually changed so it lasts longer in the body or binds its receptor more strongly.'),
  t('Approved label', 'The official prescribing information a regulator approves with a medicine, such as the EU summary of product characteristics or the US package insert. It states the approved uses, doses, contraindications and storage. On this site, label figures carry the evidence tier "Approved label".', [['Semaglutide', '/compounds/semaglutide'], ['Tirzepatide', '/compounds/tirzepatide']], 'prescribing information, SmPC'),
  t('Bacteriostatic water', 'Sterile water with a small amount of benzyl alcohol added to stop bacteria from growing, so a vial can be used more than once. It is one of the diluents used to reconstitute freeze-dried peptides.', [['Reconstitution calculator', '/tools/reconstitution-calculator']]),
  t('Bioavailability', 'The share of a dose that reaches the bloodstream unchanged. A dose injected into a vein has full bioavailability; a dose swallowed or placed under the skin usually has less.'),
  t('Bioregulator peptide', 'A label used, mainly in Russian research, for very short peptides of two to four amino acids proposed to act on gene expression in particular tissues. Epitalon, pinealon and cartalax belong to this group.', [['Epitalon', '/compounds/epitalon'], ['Pinealon', '/compounds/pinealon'], ['Cartalax', '/compounds/cartalax']]),
  t('BMI', 'Body mass index: weight in kilograms divided by height in metres squared. Obesity trials usually enrol people with a BMI of 30 or more, or 27 or more with a weight-related condition.', undefined, 'body mass index'),
  t('Certificate of analysis', 'A document from a laboratory reporting what a batch contains: identity, purity, usually by HPLC, and often mass. It describes one batch, so it is only as reliable as the laboratory that issued it.', undefined, 'COA'),
  t('Cmax', 'The highest concentration a compound reaches in the blood after a dose. Read together with Tmax, the time it takes to get there.'),
  t('Contraindication', 'A situation in which a medicine should not be used, because the risk clearly outweighs any benefit. Contraindications appear on approved labels; compounds without a label have none officially defined.'),
  t('Cycle', 'A word from user communities for a period of taking a compound, often followed by a break. Studies do not use it. They report the treatment duration, which is what this site lists.', [['Peptide cycle length', '/cycles']]),
  t('Double-blind', 'A trial design in which neither the participants nor the researchers assessing them know who received the compound and who received placebo, so expectations cannot colour the results.'),
  t('eGFR', 'Estimated glomerular filtration rate: a measure of kidney function calculated from a blood test, in mL/min per 1.73 m². Trials often exclude people below a set eGFR.', undefined, 'estimated glomerular filtration rate'),
  t('Exclusion criteria', 'The conditions that keep a person out of a trial, such as pregnancy, kidney disease or a recent heart attack. They show where a study\'s evidence stops, which is why each compound page lists them under "who should avoid".'),
  t('GH secretagogue', 'A compound that makes the pituitary gland release growth hormone, usually by acting on the ghrelin receptor. Ipamorelin and GHRP-6 are examples.', [['Ipamorelin', '/compounds/ipamorelin'], ['GHRP-6', '/compounds/ghrp-6']], 'GHS'),
  t('GHRH analogue', 'A modified form of growth hormone-releasing hormone, the brain\'s signal for the pituitary to release growth hormone. Sermorelin, tesamorelin and CJC-1295 are GHRH analogues.', [['Sermorelin', '/compounds/sermorelin'], ['Tesamorelin', '/compounds/tesamorelin'], ['CJC-1295', '/compounds/cjc-1295']]),
  t('GIP', 'Glucose-dependent insulinotropic polypeptide, a gut hormone released after eating that increases insulin release. Tirzepatide and retatrutide activate its receptor as well as the GLP-1 receptor.', [['Tirzepatide', '/compounds/tirzepatide'], ['Retatrutide', '/compounds/retatrutide']]),
  t('GLP-1 receptor agonist', 'A drug that activates the receptor for glucagon-like peptide-1, a gut hormone that increases insulin release, slows stomach emptying and reduces appetite. Semaglutide is one; tirzepatide, retatrutide and survodutide combine it with other receptors.', [['Semaglutide', '/compounds/semaglutide'], ['Survodutide', '/compounds/survodutide']]),
  t('Glucagon receptor agonist', 'A drug that activates the receptor for glucagon, a hormone that raises blood sugar and increases energy use by the liver. Retatrutide and survodutide include this action alongside GLP-1.', [['Retatrutide', '/compounds/retatrutide'], ['Survodutide', '/compounds/survodutide']]),
  t('Half-life', 'The time it takes for the amount of a compound in the blood to fall by half. It sets how often a dose is given: a half-life of hours suggests daily dosing, a half-life of days allows weekly dosing.', undefined, 'elimination half-life, t½'),
  t('HbA1c', 'Glycated haemoglobin: a blood test reflecting average blood sugar over roughly the previous two to three months. It is the main outcome in diabetes trials.', undefined, 'glycated haemoglobin'),
  t('IGF-1', 'Insulin-like growth factor 1, a hormone made mainly in the liver in response to growth hormone. Trials of growth hormone-releasing compounds measure it as a marker of their effect.', [['IGF-1 LR3', '/compounds/igf-1-lr3']]),
  t('In vitro', 'Latin for "in glass": an experiment on cells or tissue in a dish, not in a living animal or person. On this site these findings carry the tier "Mechanistic / in vitro".'),
  t('In vivo', 'An experiment in a living organism, animal or human.'),
  t('Intranasal', 'Given as drops or spray into the nose. Semax and selank are studied this way.', [['Semax', '/compounds/semax'], ['Selank', '/compounds/selank']]),
  t('IU', 'International unit: a measure of biological activity rather than weight, used for some hormones. The conversion from IU to milligrams differs from one substance to another.', [['Unit converter', '/tools/unit-converter']], 'international unit'),
  t('Lyophilised', 'Freeze-dried. Most research peptides are supplied as a lyophilised powder that is reconstituted with a liquid before use.', undefined, 'freeze-dried'),
  t('mcg and mg', 'Micrograms and milligrams. One milligram is 1,000 micrograms. Many peptide doses in studies are in micrograms, and confusing the two is a thousandfold error.', [['Unit converter', '/tools/unit-converter']], 'µg'),
  t('Melanocortin receptor agonist', 'A compound that activates melanocortin receptors, which are involved in skin pigmentation, appetite and sexual function. Bremelanotide and melanotan II act this way.', [['Bremelanotide', '/compounds/bremelanotide-pt-141'], ['Melanotan II', '/compounds/melanotan-ii']]),
  t('Meta-analysis', 'A study that pools the results of several earlier studies to give one overall estimate. It is only as strong as the studies it pools.'),
  t('Mitochondria-targeted peptide', 'A peptide designed to concentrate in mitochondria, the energy-producing parts of cells. SS-31, also called elamipretide, is one.', [['SS-31', '/compounds/ss-31'], ['MOTS-c', '/compounds/mots-c']]),
  t('Open-label', 'A trial in which everyone knows what is being given. It is often used for extension phases after a blinded trial, and its results are more open to bias.'),
  t('Peptide', 'A short chain of amino acids, the building blocks of proteins. Most compounds on this site are peptides of between two and about fifty amino acids.'),
  t('Pharmacokinetics', 'How the body absorbs, distributes, breaks down and removes a compound over time, measured by Cmax, Tmax, half-life and bioavailability.', undefined, 'PK'),
  t('Phase 1, 2 and 3 trials', 'The stages of testing in people. Phase 1 checks safety and dosing in small groups, phase 2 tests effect and dose in a few hundred people, and phase 3 confirms benefit and safety in larger groups before a regulator decides on approval.'),
  t('Placebo', 'An inactive substance given in the same way as the compound under test, so its effect can be separated from expectation and natural change.'),
  t('Preclinical', 'Research done before any testing in people: cell and animal studies. On this site animal findings carry the tier "Animal / preclinical".'),
  t('Randomized controlled trial', 'A trial in which people are assigned by chance to the compound or to a comparison, usually placebo. It is the strongest single design for showing that a compound caused an effect.', undefined, 'RCT'),
  t('Reconstitution', 'Dissolving a freeze-dried powder in a measured volume of liquid. The volume added sets the concentration, and so how much liquid holds a given dose.', [['Reconstitution calculator', '/tools/reconstitution-calculator'], ['Dosage calculators', '/calculators']]),
  t('Research use only', 'A labelling term for chemicals sold for laboratory research and not approved for use in people. It says nothing about purity or safety.', undefined, 'RUO'),
  t('Subcutaneous', 'Injected into the fatty layer just under the skin, usually of the abdomen or thigh. Most peptides studied by injection are given this way.', [['Injection sites guide', '/blog/subcutaneous-injection-sites']], 'SC, subQ'),
  t('Systematic review', 'A review that searches for every study on a question using a stated method, then appraises them. It may or may not include a meta-analysis.'),
  t('Titration', 'Raising a dose in steps over weeks so the body can adapt, which reduces side effects such as nausea. GLP-1 trials titrate from a low starting dose to the target dose.', undefined, 'dose escalation'),
  t('Tmax', 'The time from a dose to the highest blood concentration, Cmax.'),
  t('U-100 syringe', 'An insulin syringe marked in units, where 100 units equal 1 mL. Calculators on this site convert a volume into these units.', [['Reconstitution calculator', '/tools/reconstitution-calculator']], 'insulin units'),
];


// Terms worth a link from prose, with the spellings prose uses. The first
// mention on a page links to its glossary entry, at most `max` per page, after
// record links have been placed (a link is never nested in another).
const PROSE: Array<[id: string, pattern: string]> = [
  ['half-life', 'half[- ]li(?:fe|ves)'],
  ['titration', 'titrat(?:ion|ed)|dose escalation'],
  ['subcutaneous', 'subcutaneous(?:ly)?'],
  ['bioavailability', 'bioavailab(?:ility|le)'],
  ['pharmacokinetics', 'pharmacokinetics?'],
  ['placebo', 'placebo'],
  ['double-blind', 'double[- ]blind(?:ed)?'],
  ['open-label', 'open[- ]label'],
  ['randomized-controlled-trial', 'randomi[sz]ed controlled trials?'],
  ['meta-analysis', 'meta[- ]analys[ie]s'],
  ['exclusion-criteria', 'exclusion criteria'],
  ['reconstitution', 'reconstitut(?:ion|ed|e)'],
  ['lyophilised', 'lyophili[sz]ed|freeze[- ]dried'],
  ['bacteriostatic-water', 'bacteriostatic water'],
  ['hba1c', 'HbA1c'],
  ['egfr', 'eGFR'],
  ['glp-1-receptor-agonist', 'GLP-1 receptor agonists?'],
  ['gh-secretagogue', 'growth hormone secretagogues?|GH secretagogues?'],
  ['ghrh-analogue', 'GHRH analog(?:ue)?s?'],
  ['research-use-only', 'research use only'],
  ['certificate-of-analysis', 'certificates? of analysis'],
  ['in-vitro', 'in vitro'],
  ['intranasal', 'intranasal(?:ly)?'],
  ['contraindication', 'contraindicat(?:ion|ions|ed)'],
];
const known = new Set(TERMS.map((x) => x.id));
const GLOSS_TARGETS: Target[] = PROSE.filter(([id]) => known.has(id))
  .map(([id, pattern]) => ({ pattern, href: `/glossary#${id}`, key: `gloss:${id}`, flags: 'i' }));

export const glossaryLinker = (max = 4) => linker(GLOSS_TARGETS, max);
