// Splits a drafted claim into the parts the v2 card renders separately:
// study context (design, species, n, year), any structured extract the
// drafter prepended ("doses stated in the abstract: 2·4 mg"), and the verbatim
// quotation. Non-extractive claims come back as plain text.
export interface Claim { value: string; evidence_label: string; source_ids: string[]; source_excerpt?: string; drafting?: string }
export interface Parsed { design: string; species: string; n: string; year: string; extra: string; quote: string | null; text: string }

export function parseClaim(c: Claim): Parsed {
  const ex = c.source_excerpt ?? '';
  let lead = c.value, quote: string | null = null;
  if (c.drafting === 'extractive' && ex) {
    const i = c.value.indexOf(ex.slice(0, 40));
    if (i > 0) { lead = c.value.slice(0, i).trim(); quote = ex; }
    else if (c.value.endsWith('…')) { lead = c.value.slice(0, c.value.lastIndexOf(':') + 1).trim(); quote = ex; }
  }
  if (!quote) return { design: '', species: '', n: '', year: '', extra: '', quote: null, text: c.value };
  const m = lead.match(/^(.*?):\s*(.*)$/s);
  const meta = m ? m[1] : lead.replace(/:$/, '');
  const extra = m ? m[2].trim().replace(/[:.]$/, '') : '';
  const bits = meta.split(/,\s*/);
  const design = bits[0] ?? '';
  const n = (bits.find((b) => /^n=/.test(b)) ?? '').replace('n=', '');
  const year = bits.find((b) => /^\d{4}$/.test(b)) ?? '';
  const species = bits.filter((b) => b !== design && !/^n=/.test(b) && !/^\d{4}$/.test(b)).join(', ');
  return { design, species, n, year, extra, quote, text: c.value };
}

export const TIER_SHORT: Record<string, string> = {
  'approved-label': 'Approved label', 'human-clinical-trial': 'Human clinical trial', 'observational-human': 'Observational, human',
  'animal-preclinical': 'Animal, preclinical', 'mechanistic-in-vitro': 'Mechanistic, in vitro', 'community-reported': 'Community-reported',
};
