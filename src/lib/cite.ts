// Numbered citation marks. A page's Sources list is numbered in ledger order
// (components/v2/Sources.astro), so source N on the page is d.sources[N-1] and
// its anchor is its id. Claims show plain-English text followed by [N]; the
// verbatim abstract sentence stays in the record for review, not on the page.
const escHtml = (s: string) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

export function citer(sources: Array<{ id: string }>) {
  const num = new Map(sources.map((s, i) => [s.id, i + 1]));
  /** `[3]` or `[3, 7]` as linked superscript; empty when no id is in the ledger. */
  const marks = (ids: string[] = []) => {
    const known = [...new Set(ids)].filter((id) => num.has(id)).sort((a, b) => num.get(a)! - num.get(b)!);
    if (!known.length) return '';
    return `<sup class="cite">[${known.map((id) => `<a href="#${id}" aria-label="Source ${num.get(id)}">${num.get(id)}</a>`).join(', ')}]</sup>`;
  };
  /** Plain text of a claim, escaped, with its marks after it. */
  const sentence = (text: string, ids: string[] = []) => `${escHtml(text)}${marks(ids)}`;
  /** Prose written with {{cite:pmid-…}} tokens: each token becomes its mark. */
  const tokens = (html: string) => html.replace(/\{\{cite:([\w.-]+)\}\}/g, (_m, id) => marks([id]));
  return { marks, sentence, tokens, number: (id: string) => num.get(id) };
}

/** What a reader sees for a claim: the plain-English version when written, else its value. */
export const plainOf = (c: { plain?: string; value: string }) => (c.plain ?? c.value);

/** A claim whose plain version begins "Background:" reports nothing about the
 * compound itself (an off-topic paper, or an aim with no result). It stays in
 * the record for the reviewer and is not shown as evidence. */
export const isFinding = (c: any) => !(typeof c?.plain === 'string' && /^Background\b/.test(c.plain));
export const findingsOnly = (attrs: Record<string, any>) =>
  Object.fromEntries(Object.entries(attrs ?? {}).map(([k, v]) => [k, Array.isArray(v) && k !== 'protocol' ? v.filter(isFinding) : v]));
