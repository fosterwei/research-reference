// @ts-check
import { defineConfig } from 'astro/config';
import { resolveSiteUrl } from './site-url.mjs';

// Canonical tags, the sitemap and JSON-LD all derive from `site`, so it must be
// the final production origin. SITE_URL is preferred; see site-url.mjs for the
// fallbacks and the normalisation that makes a bare host or an empty value safe.
const site = resolveSiteUrl();
console.log(`[config] site origin: ${site}`);

export default defineConfig({
  site,
  output: 'static',
  trailingSlash: 'never',
  build: { format: 'directory' },
});
