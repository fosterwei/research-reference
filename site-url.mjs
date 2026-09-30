// Resolve the canonical site origin for astro.config.mjs.
//
// Astro rejects anything that is not a full URL, and environment variables are
// exactly where a bare host ("my-site.vercel.app"), a trailing slash, or an
// empty string arrive from. Accept all of those. Fall back to the production
// host Vercel injects into every build, so a deploy works with no variables
// set at all and canonicals still point at the right origin. The fallback is
// the production domain, so a build with no environment at all is still
// self-consistent rather than pointing at a placeholder.
// The canonical origin. dashnaiv.com 308-redirects to the www host, so this is
// the www host: a canonical must be the URL that answers, not one that bounces.
const FALLBACK = 'https://www.dashnaiv.com';

export function resolveSiteUrl(env = process.env) {
  // Order matters and was wrong. VERCEL_PROJECT_PRODUCTION_URL is the project's
  // *.vercel.app host, not the custom domain, and it is always set on Vercel.
  // It therefore beat the fallback on every production build, and the live site
  // told crawlers its canonical, its og:url, its sitemap and its robots Sitemap
  // line all lived on research-reference-two.vercel.app. That host answers 200
  // with no noindex, so the effect was to hand the whole site to a subdomain
  // nobody owns the brand on. The known domain now wins, and the Vercel hosts
  // are the last resort they were meant to be.
  const candidates = [
    env.SITE_URL,                      // explicit override, always wins
    FALLBACK,                          // the domain this site is published on
    env.VERCEL_PROJECT_PRODUCTION_URL, // bare host, the project's vercel.app
    env.VERCEL_URL,                    // bare host, this deployment
  ];
  for (const raw of candidates) {
    const value = (raw ?? '').trim();
    if (!value) continue;
    const withScheme = /^[a-z][a-z0-9+.-]*:\/\//i.test(value) ? value : `https://${value}`;
    try {
      const url = new URL(withScheme);
      if (url.protocol !== 'https:' && url.protocol !== 'http:') continue;
      // A wildcard or otherwise invalid hostname parses as a URL but is not
      // one. "*.vercel.app" reached production canonicals this way.
      if (url.hostname !== 'localhost' && !/^[a-z0-9]([a-z0-9-]*[a-z0-9])?(\.[a-z0-9]([a-z0-9-]*[a-z0-9])?)+$/i.test(url.hostname)) continue;
      url.pathname = '/'; url.search = ''; url.hash = '';
      return url.origin;
    } catch {
      continue;
    }
  }
  return FALLBACK;
}
