// Which compounds get their own calculator page, and the dose figures that make
// each one different from the generic tool.
//
// A calculator per compound is only worth a URL if the page says something the
// generic reconstitution calculator does not. The arithmetic is identical for
// every peptide, so the arithmetic cannot be the differentiator. What differs is
// the doses that published studies actually used, which this site already holds
// as cited claims on each record.
//
// So a compound qualifies only when it carries at least two distinct quoted dose
// figures, and only when its own record is finished and reviewed. Everything
// else would be the same page with the name changed, which is how a programmatic
// set turns into index bloat.
import type { CollectionEntry } from 'astro:content';
import { isIndexable } from './site';

export const MIN_DISTINCT_DOSES = 2;

const DOSE_FIGURE = /\d+(?:[.,]\d+)?\s*(?:mg|µg|mcg|ug|ng|IU|units?)\b/gi;

export interface DoseRow {
  value: string;
  tier: string;
  sourceIds: string[];
  excerpt?: string;
}

/** Distinct dose figures quoted anywhere in the record's study_doses claims. */
export function doseFigures(entry: CollectionEntry<'compounds'>): string[] {
  const claims = ((entry.data as any).attributes?.study_doses ?? []) as any[];
  const seen = new Set<string>();
  for (const c of claims) {
    for (const m of String(c.value ?? '').matchAll(DOSE_FIGURE)) {
      seen.add(m[0].replace(/\s+/g, ' ').trim().toLowerCase());
    }
  }
  return [...seen];
}

export function doseRows(entry: CollectionEntry<'compounds'>): DoseRow[] {
  const claims = ((entry.data as any).attributes?.study_doses ?? []) as any[];
  return claims.map((c) => ({
    value: String(c.value ?? ''),
    tier: String(c.evidence_label ?? 'editorial'),
    sourceIds: (c.source_ids ?? []) as string[],
    excerpt: c.source_excerpt,
  }));
}

/** True when a compound earns its own calculator page. */
export function qualifies(entry: CollectionEntry<'compounds'>): boolean {
  return isIndexable(entry) && doseFigures(entry).length >= MIN_DISTINCT_DOSES;
}

/** Human-tier dose claims, which are the ones worth leading with. */
export const HUMAN_TIERS = new Set(['approved-label', 'human-clinical-trial', 'observational-human']);
export function humanDoseRows(entry: CollectionEntry<'compounds'>): DoseRow[] {
  return doseRows(entry).filter((r) => HUMAN_TIERS.has(r.tier));
}

/* ------------------------------------------------------------------ *
 * The reconstitution chart
 *
 * Search intent for "<peptide> calculator" is mostly one question asked
 * in different words: how many units is this dose, in this vial, with
 * this much water. People want to read that off a table, not type it in,
 * which is why every page that ranks for these queries has a chart and
 * the first version of these pages did not.
 *
 * The chart is arithmetic, so it needs no new evidence. What makes it
 * specific to a compound is its rows: the absolute doses that studies of
 * that compound actually administered, rather than a generic ladder.
 * ------------------------------------------------------------------ */

/** Absolute mass doses, in micrograms, as quoted in a record's claims.
 *  Per-kilogram figures are excluded: they do not convert to a person. */
export function absoluteDosesMcg(entry: CollectionEntry<'compounds'>): number[] {
  const claims = ((entry.data as any).attributes?.study_doses ?? []) as any[];
  const out = new Set<number>();
  for (const c of claims) {
    const text = String(c.value ?? '');
    // "10 µg/kg", "0.2 mg/kg" and friends are per-weight; skip the whole match.
    const re = /(\d+(?:\.\d+)?)\s*(mg|µg|mcg|ug)\b(\s*\/\s*kg)?/gi;
    for (const m of text.matchAll(re)) {
      if (m[3]) continue;
      const n = parseFloat(m[1]);
      if (!Number.isFinite(n) || n <= 0) continue;
      const mcg = /mg/i.test(m[2]) ? n * 1000 : n;
      if (mcg >= 1 && mcg <= 100_000) out.add(Math.round(mcg * 100) / 100);
    }
  }
  return [...out].sort((a, b) => a - b).slice(0, 8);
}

export const VIAL_MG = [2, 5, 10] as const;
export const DILUENT_ML = [1, 2, 3] as const;

export interface ChartCell { ml: number; units: number; }
export interface ChartRow { mcg: number; label: string; cells: ChartCell[]; }

export function formatDose(mcg: number): string {
  return mcg >= 1000
    ? `${(mcg / 1000).toLocaleString('en-US', { maximumFractionDigits: 3 })} mg`
    : `${mcg.toLocaleString('en-US', { maximumFractionDigits: 2 })} mcg`;
}

/** Units on a U-100 syringe for each diluent volume, at one vial size. */
export function chartRows(doses: number[], vialMg: number): ChartRow[] {
  return doses.map((mcg) => ({
    mcg,
    label: formatDose(mcg),
    cells: DILUENT_ML.map((ml) => {
      const concMcgPerMl = (vialMg * 1000) / ml;
      const drawMl = mcg / concMcgPerMl;
      return { ml, units: Math.round(drawMl * 100 * 100) / 100 };
    }),
  }));
}

/** Claims from any attribute, shaped like doseRows. */
export function claimRows(entry: CollectionEntry<'compounds'>, key: string): DoseRow[] {
  const claims = ((entry.data as any).attributes?.[key] ?? []) as any[];
  return claims.map((c) => ({
    value: String(c.value ?? ''),
    tier: String(c.evidence_label ?? 'editorial'),
    sourceIds: (c.source_ids ?? []) as string[],
    excerpt: c.source_excerpt,
  }));
}
