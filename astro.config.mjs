// @ts-check
import { defineConfig } from 'astro/config';

// SITE_URL is set in Vercel project settings (and in .env locally). Canonical
// tags, the sitemap and JSON-LD all derive from it, so it must be the final
// production origin with no trailing slash.
const site = process.env.SITE_URL ?? 'https://example.com';

export default defineConfig({
  site,
  output: 'static',
  trailingSlash: 'never',
  build: { format: 'directory' },
});
