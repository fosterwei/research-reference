// Automatic entity linking for a page's own prose.
//
// Every audit run since ipamorelin logged the same partial accept-template:
// internal link density sits near 1 per 1,000 words against a 3-to-5 target,
// because links are added by hand while writing and a writer cannot remember
// forty-five records. This links the first mention of each other record in a
// page's guide prose, once per target, under a page-wide cap.
//
// Rules, in order of importance:
//   - never inside an existing link, a quotation, a heading or code;
//   - never the page's own subject, which would link to itself;
//   - the longest matching name wins, so "Melanotan II" beats "melanotan";
//   - one added link per target per page, and at most `max` added links, so a
//     page does not turn blue; a target the writer linked by hand may still
//     gain one automatic link elsewhere, which is how a comparison table row
//     becomes clickable on a page that linked the same record in prose;
//   - the matched text is left exactly as written, only wrapped.
import { compounds, stacks, tools } from './registry';

export interface Target { pattern: string; href: string; key: string }

const ESC = /[.*+?^${}()|[\]\\]/g;
const esc = (s: string) => s.replace(ESC, '\\$&');

/** Name and aliases of every record, longest first. */
function allTargets(): Target[] {
  const out: Target[] = [];
  for (const c of compounds) {
    const names = [c.name, ...(c.aliases ?? [])].filter((n) => n && n.length >= 4);
    for (const n of names) out.push({ pattern: esc(n).replace(/\\?[-\s]/g, '[-\\s]'), href: `/compounds/${c.slug}`, key: c.slug });
  }
  for (const s of stacks) out.push({ pattern: esc(s.name).replace(/\\?[-\s]/g, '[-\\s]'), href: `/stacks/${s.slug}`, key: `stack:${s.slug}` });
  // Comparison records are not auto-linked: their names are phrases ("X vs Y")
  // that prose writes a dozen ways, and a wrong link is worse than none.
  for (const t of tools) if (t.name) out.push({ pattern: esc(t.name).replace(/\\?[-\s]/g, '[-\\s]'), href: `/tools/${t.slug}`, key: `tool:${t.slug}` });
  return out
    .filter((t) => t.pattern && t.href)
    .sort((a, b) => b.pattern.length - a.pattern.length);
}

const TARGETS = allTargets();
const SKIP = /^(?:a|q|code|pre|h1|h2|h3|h4|abbr|time|caption|mark)$/i;

/**
 * Returns a linker with page-wide state: call it on each guide section's HTML
 * in document order, and it spends one budget across the whole page.
 */
export function entityLinker(excludeKeys: string[] = [], max = 10) {
  const skip = new Set(excludeKeys);
  const used = new Set<string>();
  let added = 0;
  const targets = TARGETS.filter((t) => !skip.has(t.key) && !skip.has(t.href));

  return function link(html: string): string {
    if (!html || added >= max) return html;
    let depth = 0;
    return html.replace(/<[^>]*>|[^<]+/g, (token) => {
      if (token.startsWith('<')) {
        const m = /^<(\/?)\s*([a-zA-Z0-9]+)/.exec(token);
        if (m && SKIP.test(m[2])) {
          if (m[1]) depth = Math.max(0, depth - 1);
          else if (!token.endsWith('/>')) depth += 1;
        }
        return token;
      }
      if (depth > 0 || added >= max) return token;
      // Collect one match per target first, then splice right to left, so an
      // inserted href can never be matched by a later pattern.
      const hits: Array<{ start: number; end: number; href: string; key: string }> = [];
      // Two aliases of one compound can sit in the same sentence ("SS-31
      // (elamipretide)"); the target is taken by the first of them.
      const taken = new Set<string>();
      for (const t of targets) {
        if (used.has(t.key) || taken.has(t.key) || added + hits.length >= max) continue;
        const re = new RegExp(`(?<![\\w-])(?:${t.pattern})(?![\\w-])`);
        const m = re.exec(token);
        if (!m) continue;
        if (hits.some((h) => m.index < h.end && h.start < m.index + m[0].length)) continue;
        hits.push({ start: m.index, end: m.index + m[0].length, href: t.href, key: t.key });
        taken.add(t.key);
      }
      if (!hits.length) return token;
      hits.sort((a, b) => b.start - a.start);
      let out = token;
      for (const h of hits) {
        out = `${out.slice(0, h.start)}<a href="${h.href}">${out.slice(h.start, h.end)}</a>${out.slice(h.end)}`;
        used.add(h.key);
        added += 1;
      }
      return out;
    });
  };
}
