// Only published records enter the sitemap, and lastmod is the record's own
// last changelog date. Both rules come from docs/content-contract.md and both
// were failures in the competitor audit.
import type { APIRoute } from 'astro';
import { records } from '../lib/collections';
import { isIndexable, lastmod } from '../lib/site';

const PREFIX = { compounds: '/compounds/', stacks: '/stacks/', comparisons: '/compare/', tools: '/tools/', posts: '/blog/' } as const;

export const GET: APIRoute = async ({ site }) => {
  const urls: string[] = [];
  for (const [name, prefix] of Object.entries(PREFIX) as Array<[keyof typeof PREFIX, string]>) {
    for (const entry of await records(name)) {
      if (!isIndexable(entry)) continue;
      const loc = new URL(`${prefix}${entry.data.slug}`, site).toString();
      const mod = lastmod(entry);
      urls.push(`<url><loc>${loc}</loc>${mod ? `<lastmod>${mod}</lastmod>` : ''}</url>`);
    }
  }
  const xml = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${urls.join('\n')}\n</urlset>\n`;
  return new Response(xml, { headers: { 'Content-Type': 'application/xml; charset=utf-8' } });
};
