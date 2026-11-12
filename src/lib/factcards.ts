// Written sections already carry their structure in the prose: paragraphs
// and list items that open with a bold lead-in ("<strong>What it is.</strong>
// …"). This turns each such run into a grid of labelled cards, the lead-in
// as the label and the rest as the body, without changing a word. Paragraphs
// without a lead-in, tables and cards pass through untouched. A paragraph
// that is only a lead-in ("<strong>Cautions that recur.</strong>") becomes a
// small heading for the cards that follow.
const trimLabel = (s: string) => s.replace(/\s*[.:]\s*$/, '').trim();
const card = (label: string, body: string) => `<div class="fc"><dt>${trimLabel(label)}</dt><dd>${body.trim()}</dd></div>`;

export function factCards(html: string): string {
  let out = html.replace(/<p>\s*<strong>(.*?)<\/strong>\s*([\s\S]*?)<\/p>/g, (_m, label: string, rest: string) =>
    rest.trim() ? card(label, rest) : `<h3 class="fc-head">${trimLabel(label)}</h3>`);
  out = out.replace(/<(ul|ol)>([\s\S]*?)<\/\1>/g, (m, _tag: string, inner: string) => {
    const items = inner.match(/<li>[\s\S]*?<\/li>/g) ?? [];
    if (items.length === 0 || !items.every((li) => /^<li>\s*<strong>/.test(li))) return m;
    return items.map((li) => li.replace(/^<li>\s*<strong>(.*?)<\/strong>\s*([\s\S]*?)<\/li>$/, (_x, label: string, rest: string) => card(label, rest))).join('');
  });
  // Adjacent cards share one grid.
  return out.replace(/((?:<div class="fc"><dt>[\s\S]*?<\/dd><\/div>\s*)+)/g, (run) => `<dl class="fcards">${run.trim()}</dl>`);
}
