// Resolve the canonical site origin for astro.config.mjs.
//
// Astro rejects anything that is not a full URL, and environment variables are
// exactly where a bare host ("my-site.vercel.app"), a trailing slash, or an
// empty string arrive from. Accept all of those. Fall back to the production
// host Vercel injects into every build, so a deploy works with no variables
// set at all and canonicals still point at the right origin.
const FALLBACK = 'https://example.com';

export function resolveSiteUrl(env = process.env) {
  const candidates = [
    env.SITE_URL,
    env.VERCEL_PROJECT_PRODUCTION_URL, // bare host, production domain
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
