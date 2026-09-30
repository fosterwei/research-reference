// robots.txt. Nothing is disallowed, and that is deliberate.
//
// The pages this site keeps out of search are kept out with a noindex meta tag,
// which only works if a crawler is allowed to fetch the page and read it. The
// seven unwritten records and the 404 are noindex for that reason. Adding a
// Disallow for them would have the opposite of the intended effect: the tag
// would never be seen, and the URLs could still be indexed from links pointing
// at them, with no description.
//
// There is also nothing else to block. The site is static, has no search, no
// parameters, no session URLs and no faceted navigation, so there are no crawl
// traps. The bundled CSS and JS under /_astro must stay fetchable or Google
// cannot render the pages.
//
// scripts/check_links.py fails the build if a Disallow rule here ever blocks a
// URL the sitemap advertises, or if the Sitemap line names a different origin
// from the one the build used.
import type { APIRoute } from 'astro';

export const GET: APIRoute = ({ site }) =>
  new Response(
    [
      'User-agent: *',
      'Allow: /',
      '',
      `Sitemap: ${new URL('/sitemap.xml', site)}`,
      '',
    ].join('\n'),
    { headers: { 'Content-Type': 'text/plain; charset=utf-8' } },
  );
