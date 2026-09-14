// Vercel Edge Middleware. Runs before the static file is served.
//
// Every slug in data/ is lowercase and hyphenated, but peptide names are
// routinely written in capitals, so inbound links like /compounds/BPC-157 are
// common. The competitor audit found the incumbent sends those to a
// "coming soon" placeholder. We send them, permanently, to the real page.
export default function middleware(request: Request): Response | undefined {
  const url = new URL(request.url);
  const lower = url.pathname.toLowerCase();
  if (lower !== url.pathname) {
    url.pathname = lower;
    return Response.redirect(url.toString(), 301);
  }
  return undefined;
}

export const config = {
  // Static assets carry hashed, case-sensitive names; leave them alone.
  matcher: ['/((?!_astro/|favicon\\.ico|robots\\.txt|sitemap\\.xml).*)'],
};
