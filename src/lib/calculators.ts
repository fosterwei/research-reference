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
