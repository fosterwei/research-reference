// One line that says what a per-study section holds, computed from the
// figures the drafter extracted into each claim ("doses stated in the
// abstract: 20 mg", "administration by oral route reported", "durations
// stated: 3 months", "weight-normalized doses as published: 10 µg/kg/day").
// The line restates those figures grouped by species, people first, and
// carries the marks of every study it draws on; the per-study rows stay on
// the page beneath it. Nothing is inferred: a figure appears only if a claim
// states it, and a section whose claims lack the structured prefix gets no
// digest and keeps its first cited sentence as the answer.
import { parseClaim, type Claim } from './claims';

const LABEL: Record<string, (n: number) => string> = {
  study_doses: (n) => `Doses stated in ${n} ${n === 1 ? 'study' : 'studies'}:`,
  study_durations: (n) => `Durations stated in ${n} ${n === 1 ? 'study' : 'studies'}:`,
  routes_studied: (n) => `Routes in ${n} ${n === 1 ? 'study' : 'studies'}:`,
  weight_normalized_doses: (n) => `Per-kilogram doses in ${n} ${n === 1 ? 'study' : 'studies'}:`,
};

const figureOf = (field: string, extra: string): string | undefined => {
  if (!extra) return undefined;
  if (field === 'routes_studied') return extra.match(/administration by (.+?) route/i)?.[1]?.toLowerCase();
  const i = extra.indexOf(':');
  if (i < 0) return undefined;
  const v = extra.slice(i + 1).trim();
  return v && !/^not stated/i.test(v) ? v : undefined;
};

const speciesLabel = (s: string) => {
  const t = s.toLowerCase().replace(/\s*\(.*?\)/g, '').trim();
  if (!t) return 'species not stated';
  if (t === 'humans' || t === 'human') return 'people';
  return t;
};

/** HTML for the digest line, or undefined when fewer than half the claims carry a figure. */
export function digest(field: string, claims: Claim[], marks: (ids: string[]) => string): string | undefined {
  const label = LABEL[field];
  if (!label || claims.length === 0) return undefined;
  const groups = new Map<string, { figures: string[]; ids: string[] }>();
  let counted = 0;
  for (const c of claims) {
    const p = parseClaim(c);
    const fig = figureOf(field, p.extra);
    if (!fig) continue;
    counted += 1;
    const g = speciesLabel(p.species);
    const slot = groups.get(g) ?? { figures: [], ids: [] };
    for (const f of fig.split(/;\s*/)) if (f && !slot.figures.includes(f)) slot.figures.push(f);
    for (const id of c.source_ids) if (!slot.ids.includes(id)) slot.ids.push(id);
    groups.set(g, slot);
  }
  if (counted === 0 || counted * 2 < claims.length) return undefined;
  const esc = (s: string) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  const ordered = [...groups.entries()].sort((a, b) => (a[0] === 'people' ? -1 : b[0] === 'people' ? 1 : b[1].figures.length - a[1].figures.length));
  const parts = ordered.map(([g, s]) => `<b>${esc(g)}</b> ${s.figures.map(esc).join(', ')}${marks(s.ids)}`);
  return `${label(counted)} ${parts.join('; ')}.`;
}
