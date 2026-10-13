// Only indexable pages enter the sitemap, and every entry carries a lastmod
// that moves when, and only when, the page's content changed.
//
// Two sources, never mixed for one page:
//
//   Records (compounds, stacks, comparisons, tools) use their own latest
//   changelog date. Those pages print that date three times, in the Updated
//   pill, the reference card and JSON-LD dateModified, and the sitemap has to
//   agree with the page or Google learns to ignore it.
//
//   Everything else (the homepage, the directories, the trust pages and the
//   per-compound calculators) prints no date of its own, so its lastmod lives
//   in research/lastmod.json, maintained by scripts/check_lastmod.py.
//
// The build never stamps today's date: a sitemap where every URL changed on
// every deploy tells a crawler nothing.
import fs from 'node:fs';
import path from 'node:path';
import type { APIRoute } from 'astro';
import { records } from '../lib/collections';
import { isIndexable, lastmod } from '../lib/site';
import { qualifies } from '../lib/calculators';

const PREFIX = { compounds: '/compounds/', stacks: '/stacks/', comparisons: '/compare/', tools: '/tools/', posts: '/blog/' } as const;

// Rendered pages that are not records. Listed by hand, because a page that
// should not be indexed must not be listed, and that is a decision per page.
const STATIC = ['/', '/compounds', '/stacks', '/compare', '/tools', '/calculators', '/about', '/contact', '/privacy'];

type Manifest = { pages?: Record<string, { lastmod?: string }> };
const manifest: Manifest = (() => {
  try {
    return JSON.parse(fs.readFileSync(path.resolve(process.cwd(), 'research', 'lastmod.json'), 'utf8'));
  } catch {
    return {};
  }
})();
const tracked = (p: string) => manifest.pages?.[p]?.lastmod;

const entry = (loc: string, mod?: string) => `<url><loc>${loc}</loc>${mod ? `<lastmod>${mod}</lastmod>` : ''}</url>`;

export const GET: APIRoute = async ({ site }) => {
  const urls: string[] = [];
  for (const p of STATIC) urls.push(entry(new URL(p, site).toString(), tracked(p)));

  for (const [name, prefix] of Object.entries(PREFIX) as Array<[keyof typeof PREFIX, string]>) {
    for (const e of await records(name)) {
      if (!isIndexable(e)) continue;
      urls.push(entry(new URL(`${prefix}${e.data.slug}`, site).toString(), lastmod(e)));
    }
  }

  // Per-compound calculators derive from the compounds collection, so nothing
  // above emits them. Their date is their own, not the compound's: a reviewer
  // change on the record does not change the calculator page.
  for (const e of await records('compounds')) {
    if (!qualifies(e)) continue;
    const p = `/calculators/${e.data.slug}`;
    urls.push(entry(new URL(p, site).toString(), tracked(p)));
  }

  const xml = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${urls.join('\n')}\n</urlset>\n`;
  return new Response(xml, { headers: { 'Content-Type': 'application/xml; charset=utf-8' } });
};
