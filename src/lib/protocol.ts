// Shared reading of attributes.protocol (docs/content-contract.md, "Protocol
// layer"). The page shows the same reviewed records three ways, in the layout
// readers of dosing guides expect: a quick-start box, a week-by-week table, and
// FAQ answers. Every figure here is a field of a cited claim; nothing is
// computed into a new dose.
export type PClaim = { value: string; evidence_label: string; source_ids?: string[]; fields?: Record<string, string>; pending_source?: boolean };

const HUMAN = ['human-clinical-trial', 'observational-human'];
const phaseNum = (c: PClaim) => Number(c.fields?.phase) || 0;

export function splitProtocol(claims: PClaim[]) {
  return {
    label: claims.filter((c) => c.evidence_label === 'approved-label'),
    studied: claims.filter((c) => HUMAN.includes(c.evidence_label)),
    practical: claims.filter((c) => c.evidence_label === 'editorial' && c.fields?.phase !== 'note').sort((a, b) => phaseNum(a) - phaseNum(b)),
    notes: claims.filter((c) => c.evidence_label === 'editorial' && c.fields?.phase === 'note'),
  };
}

/** "1–4" reads as "Weeks 1–4"; "by week 24" as "By week 24". */
export const whenLabel = (w?: string) => !w ? '' : /^\d/.test(w) ? `Weeks ${w}` : `${w[0].toUpperCase()}${w.slice(1)}`;

const uniq = (xs: (string | undefined)[]) => [...new Set(xs.filter((x): x is string => Boolean(x && !/not stated/i.test(x))))];
const sentence = (s: string) => s.replace(/\s+$/, '').replace(/([^.])$/, '$1.');

export type Fact = { k: string; v: string; s?: string };

/** The quick-start box: what a reader scanning for "starting dose" wants first. */
export function quickStart(claims: PClaim[]): Fact[] {
  const { label, studied, practical } = splitProtocol(claims);
  const sources = uniq([...label, ...studied].flatMap((c) => c.source_ids ?? []));
  const out: Fact[] = [];
  if (practical.length) {
    const first = practical[0];
    out.push({ k: 'Starting dose', v: first.fields?.action ?? first.value, s: whenLabel(first.fields?.weeks) });
    const path = uniq(practical.map((c) => c.fields?.dose));
    out.push(path.length > 1
      ? { k: 'Titration', v: path.join(' → '), s: `${practical.length} steps` }
      : { k: 'Titration', v: 'None: one fixed dose', s: 'the trials did not step the dose' });
    const last = practical[practical.length - 1];
    out.push({ k: 'Then', v: last.fields?.action ?? last.value, s: whenLabel(last.fields?.weeks) });
  } else {
    out.push({ k: 'Doses studied in humans', v: uniq(studied.map((c) => c.fields?.dose)).slice(0, 4).join('; ') || 'not stated', s: `${studied.length} regimen${studied.length === 1 ? '' : 's'}` });
    out.push({ k: 'Practical protocol', v: 'Not written', s: 'no human study ran a repeated regimen a reader could follow' });
  }
  const freq = uniq([...practical, ...label, ...studied].map((c) => c.fields?.frequency));
  if (freq.length) out.push({ k: 'Frequency', v: freq[0], s: freq.length > 1 ? `also studied: ${freq.slice(1, 3).join('; ')}` : undefined });
  const route = uniq([...practical, ...label, ...studied].map((c) => c.fields?.route));
  if (route.length) out.push({ k: 'Route', v: route[0], s: route.length > 1 ? `also studied: ${route.slice(1, 3).join('; ')}` : undefined });
  out.push({ k: 'Evidence', v: `${label.length ? 'Approved label and ' : ''}${studied.length} human regimen${studied.length === 1 ? '' : 's'}`, s: `${sources.length} cited source${sources.length === 1 ? '' : 's'}` });
  return out;
}

/** FAQ items in the form dosing searches are phrased, answered from the same claims. */
export function protocolFaq(name: string, claims: PClaim[], cite: (ids: string[]) => string): { question: string; answer: string }[] {
  const { label, studied, practical } = splitProtocol(claims);
  const out: { question: string; answer: string }[] = [];
  if (practical.length) {
    const first = practical[0];
    out.push({ question: `What is the starting dose of ${name}?`,
      answer: `${sentence(first.fields?.action ?? '')} ${sentence(first.value)} ${cite(first.source_ids ?? [])}` });
  }
  if (practical.length > 1) {
    out.push({ question: `What is the ${name} dosing schedule?`,
      answer: practical.map((c) => `<strong>${whenLabel(c.fields?.weeks)}:</strong> ${sentence(c.fields?.action ?? '')}`).join(' ') + ` ${cite(uniq(practical.flatMap((c) => c.source_ids ?? [])))}` });
  }
  if (label.length) {
    const l = label[0].fields ?? {};
    out.push({ question: `What is the approved dose of ${name}?`,
      answer: `${sentence([l.dose, l.frequency, l.route].filter(Boolean).join(', '))} ${l.population ? `For ${l.population.replace(/^./, (m) => m.toLowerCase())}.` : ''} ${label[0].pending_source ? 'The label document is cited as pending.' : cite(label[0].source_ids ?? [])}` });
  }
  if (studied.length) {
    const rows = studied.slice(0, 5).map((c) => {
      const f = c.fields ?? {};
      const bits = [f.dose, f.frequency, f.route].filter((x) => x && !/not stated/i.test(x)).join(', ');
      const dur = f.duration && !/not stated/i.test(f.duration) ? `; ${f.duration}` : '';
      return `${bits}${dur}${f.population ? ` (${f.population.replace(/^./, (m) => m.toLowerCase())})` : ''} ${cite(c.source_ids ?? [])}`;
    });
    out.push({ question: `What doses of ${name} have been studied in humans?`,
      answer: `${rows.map((r) => sentence(r.trim())).join(' ')}${studied.length > 5 ? ` The full table on this page lists all ${studied.length}.` : ''}` });
  }
  return out;
}
