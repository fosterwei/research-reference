// Cycle length, as studies report it: how long a compound was given. Used by
// /cycles. Two inputs, both already reviewed on the compound pages:
//   - the longest treatment period among the record's human regimen rows
//     (attributes.protocol, human labels only, notes excluded), and
//   - the plain-English study-duration findings (attributes.study_durations).
// Durations parsed from claim values are never shown: the drafter's parse
// picks up ages and follow-up periods as well as treatment lengths.
import { isFinding } from './cite';

const HUMAN = new Set(['approved-label', 'human-clinical-trial', 'observational-human']);
const UNIT: Record<string, number> = { day: 1 / 7, week: 1, month: 52 / 12, year: 52 };

/** Weeks named in a duration string ("48 weeks", "12 months"); the largest wins. */
export function weeksIn(s = ''): number {
  let best = 0;
  for (const m of s.matchAll(/(\d+(?:\.\d+)?)\s*(day|week|month|year)s?\b/gi)) {
    best = Math.max(best, parseFloat(m[1]) * UNIT[m[2].toLowerCase()]);
  }
  return best;
}

export type Course = { duration: string; population?: string; ids: string[]; label: string; weeks: number };

/** The longest human course on the record's regimen rows, or null. */
export function longestHumanCourse(attrs: any): Course | null {
  let best: Course | null = null;
  for (const c of (attrs?.protocol ?? []) as any[]) {
    if (!HUMAN.has(c.evidence_label) || c.fields?.phase === 'note' || c.drafting === 'editorial') continue;
    if (/\bsingle (?:dose|injection)\b/i.test(c.fields?.duration ?? '')) continue; // a sampling window, not a course
    const w = weeksIn(c.fields?.duration);
    if (w > 0 && (!best || w > best.weeks)) best = { duration: c.fields.duration, population: c.fields?.population, ids: c.source_ids ?? [], label: c.evidence_label, weeks: w };
  }
  return best;
}

const RANK: Record<string, number> = { 'approved-label': 0, 'human-clinical-trial': 1, 'observational-human': 2, 'animal-preclinical': 3, 'mechanistic-in-vitro': 4 };

// A finding whose own wording says it gives no treatment length (an age, an
// enrolment count) is honest on the compound page but not a cycle length.
const NOT_A_DURATION = /\b(?:does not (?:state|give)|gives no|are ages|not treatment lengths?)\b/i;

/** Study-duration findings with a written plain version, human evidence first. */
export function durationFindings(attrs: any, limit = 3): any[] {
  return ((attrs?.study_durations ?? []) as any[])
    .filter((c) => isFinding(c) && typeof c.plain === 'string' && c.plain.trim() && !NOT_A_DURATION.test(c.plain))
    .sort((a, b) => (RANK[a.evidence_label] ?? 9) - (RANK[b.evidence_label] ?? 9))
    .slice(0, limit);
}
