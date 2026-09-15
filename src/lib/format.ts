// Formatting helpers for the page's own prose, per docs/design.md section 9.
// Never applied to quotations: those are verbatim and receive only the
// emphasis-added <mark> handled in ClaimCards.

export const ABBR: Record<string, string> = {
  RCTs: 'randomized controlled trials', RCT: 'randomized controlled trial',
  'GLP-1': 'glucagon-like peptide-1', MASH: 'metabolic dysfunction-associated steatohepatitis',
  AUD: 'alcohol use disorder', HbA1c: 'glycated haemoglobin', ATC: 'Anatomical Therapeutic Chemical classification',
  CKD: 'chronic kidney disease', T2D: 'type 2 diabetes', BMI: 'body mass index', PMID: 'PubMed identifier',
  ChEMBL: 'EMBL-EBI database of bioactive molecules', GIP: 'glucose-dependent insulinotropic polypeptide',
};

export function esc(s: string): string {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

const MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
export function fmtDate(iso: string): string {
  const m = /^(\d{4})-(\d{2})-(\d{2})/.exec(iso);
  if (!m) return iso;
  return `${Number(m[3])} ${MONTHS[Number(m[2]) - 1]} ${m[1]}`;
}
export function timeTag(iso: string, display?: string): string {
  return `<time datetime="${esc(iso)}">${esc(display ?? fmtDate(iso))}</time>`;
}

export interface RichOpts { bold?: number; seen?: Set<string>; abbr?: boolean }

/** Escape, then: dates to <time>, number+unit non-breaking, first N figures bold, abbreviations on first use. */
export function rich(text: string, opts: RichOpts = {}): string {
  const bold = opts.bold ?? 2;
  let s = esc(text);
  const holes: string[] = [];
  const hold = (html: string) => { holes.push(html); return `@@${holes.length - 1}@@`; };
  s = s.replace(/\b\d{4}-\d{2}-\d{2}\b/g, (d) => hold(timeTag(d)));
  s = s.replace(/(\d)\s(mg|mcg|ng|mL|kg|IU|weeks?|days?|months?|years?|residues)\b/g, '$1&nbsp;$2');
  let n = 0;
  s = s.replace(/(?<![\w&#;@-])(\d[\d,]*(?:\.\d+)?%?)(?![\w;@-])/g, (m) => (n++ < bold ? `<b>${m}</b>` : m));
  if (opts.abbr !== false) {
    for (const [k, v] of Object.entries(ABBR)) {
      if (opts.seen?.has(k)) continue;
      const re = new RegExp(`(?<![\\w-])${k.replace(/-/g, '\\-')}(?![\\w-])`);
      if (re.test(s)) { s = s.replace(re, `<abbr title="${esc(v)}">${k}</abbr>`); opts.seen?.add(k); }
    }
  }
  return s.replace(/@@(\d+)@@/g, (_m, i) => holes[Number(i)]);
}

/** Split a long paragraph at sentence boundaries into chunks of at most `max` sentences. */
export function paragraphs(text: string, max = 3): string[] {
  const sents = text.split(/(?<=[.!?])\s+(?=[A-Z])/);
  const out: string[] = [];
  for (let i = 0; i < sents.length; i += max) out.push(sents.slice(i, i + max).join(' '));
  return out;
}

/** Wrap occurrences of `terms` inside quote text with <mark>. Returns [html, marked]. */
export function markTerms(quoteText: string, terms: string[]): [string, boolean] {
  let s = esc(quoteText); let marked = false;
  for (const t of terms.map((x) => x.trim()).filter((x) => x.length >= 3)) {
    const re = new RegExp(esc(t).replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'g');
    if (re.test(s)) { s = s.replace(re, (m) => `<mark>${m}</mark>`); marked = true; }
  }
  return [s, marked];
}
