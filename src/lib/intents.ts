// Intent maps: research/intents/<slug>.json, produced by docs/content-sop.md
// stages 1–5 and consumed here at build time. A map may reorder the body of a
// page, rename sections into the searcher's phrasing, add boundary sentences
// and FAQ items, and place explicit absence statements. It can never change a
// claim, a tier or a source; those come from the record alone.
import fs from 'node:fs';
import path from 'node:path';

export type Policy = 'evidence-only' | 'evidence-with-boundary' | 'redirect' | 'decline';

export interface IntentQuery {
  query: string;
  policy: Policy;
  section?: string;          // record field (study_doses) or page block (what, faq, combination, compare)
  heading?: string;          // searcher-phrased heading for that section
  boundary?: string;         // reader-facing sentence that must open the section's lede
  answer_from?: string;      // for FAQ items: record field whose first claim answers the question
  answer?: string;           // for FAQ items: our own prose answer, when no claim answers it
  target?: string;
  volume?: { clickstream?: number | null; google_ads?: number | null; kd?: number | null; source?: string };
}

export interface IntentMap {
  slug: string;
  queries: IntentQuery[];
  outline?: string[];        // block ids in reading order; the spine is fixed regardless
  information_gain?: string;
  decline_notice?: string;
}

const ROOT = path.resolve(process.cwd(), 'research', 'intents');

export function loadIntent(slug: string): IntentMap | null {
  const file = path.join(ROOT, `${slug}.json`);
  if (!fs.existsSync(file)) return null;
  try {
    const m = JSON.parse(fs.readFileSync(file, 'utf8')) as IntentMap;
    return Array.isArray(m.queries) ? m : null;
  } catch {
    return null;
  }
}

/** Queries mapped to a record field or page block, highest demand first. */
export function queriesFor(m: IntentMap | null, section: string): IntentQuery[] {
  if (!m) return [];
  return m.queries
    .filter((q) => q.section === section)
    .sort((a, b) => (b.volume?.clickstream ?? b.volume?.google_ads ?? 0) - (a.volume?.clickstream ?? a.volume?.google_ads ?? 0));
}

export function headingFor(m: IntentMap | null, section: string, fallback: string): string {
  return queriesFor(m, section).find((q) => q.heading)?.heading ?? fallback;
}

/** The boundary sentence for a section, if any mapped query carries one. */
export function boundaryFor(m: IntentMap | null, section: string): string | null {
  return queriesFor(m, section).find((q) => q.boundary)?.boundary ?? null;
}

/**
 * Order body blocks by the map's outline. Ids not in the outline keep their
 * default relative order and follow the outlined ones; ids in the outline but
 * not renderable are dropped. The spine (title, glance, status, sources, card,
 * related, changelog) is positioned by the layout, not by this function.
 */
export function orderBlocks<T extends { id: string; group?: string }>(m: IntentMap | null, blocks: T[]): T[] {
  if (!m?.outline?.length) return blocks;
  const rank = new Map(m.outline.map((id, i) => [id, i]));
  const out = blocks.filter((b) => rank.has(b.id)).sort((a, b) => rank.get(a.id)! - rank.get(b.id)!);
  // An unlisted block joins the end of its own group (an evidence section the
  // map did not mention sits with the other evidence sections, not after the FAQ).
  for (const b of blocks.filter((x) => !rank.has(x.id))) {
    let at = -1;
    out.forEach((o, i) => { if (o.group === b.group) at = i; });
    if (at >= 0) out.splice(at + 1, 0, b); else out.push(b);
  }
  return out;
}
