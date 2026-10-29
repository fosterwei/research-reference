// Guides: editorial posts arranged as index -> pillar -> sub.
//
// Every post in a series names its place in the tree:
//   series  the series key, shared by all its pages ("cagrilintide")
//   role    'index' (one per series), 'pillar' (one per topic) or 'sub'
//   parent  the path of the page above it. A pillar's parent is the series
//           index; a sub's parent is its pillar. A pillar may also be an
//           existing programmatic page (a stack, compound or comparison), in
//           which case the index lists it and its subs point at it.
//   about   paths of programmatic records the page is about; those records
//           link back to it from their "Related records" section.
//
// The index record carries `topics`, the ordered list of pillars, so a topic
// whose pillar is not a post (e.g. /stacks/cagrisema) still has a slot.
//
// Citations: section HTML writes [[n]] after a claim; n is the 1-based
// position in the record's sources[]. cite() turns each marker into a
// superscript link straight to that source, the same "corner mark" pattern
// the series uses on Reddit. scripts/validate_content.py checks every marker
// has a source and every source is cited.
import type { CollectionEntry } from 'astro:content';
import { records } from './collections';

export type Post = CollectionEntry<'posts'>;
export type Topic = { label: string; pillar: string; blurb?: string };
export type Crumb = { name: string; path: string };

export const postPath = (slug: string) => `/blog/${slug}`;

export async function seriesPosts(series: string): Promise<Post[]> {
  return (await records('posts')).filter((p) => (p.data as any).series === series);
}

export function byOrder(a: Post, b: Post): number {
  const oa = (a.data as any).order ?? 999, ob = (b.data as any).order ?? 999;
  return oa - ob || a.data.title.localeCompare(b.data.title);
}

/** Pages whose parent is `path`, in reading order. */
export async function childrenOf(path: string, series?: string): Promise<Post[]> {
  const all = await records('posts');
  return all.filter((p) => (p.data as any).parent === path && (!series || (p.data as any).series === series)).sort(byOrder);
}

/** Posts that declare they are about a programmatic record, or hang under it. */
export async function guidesFor(path: string): Promise<Post[]> {
  const all = await records('posts');
  return all.filter((p) => {
    const d = p.data as any;
    return d.parent === path || (Array.isArray(d.about) && d.about.includes(path));
  }).sort((a, b) => {
    const r = (p: Post) => ({ index: 0, pillar: 1, sub: 2 } as Record<string, number>)[(p.data as any).role] ?? 3;
    return r(a) - r(b) || byOrder(a, b);
  });
}

export async function indexFor(series: string): Promise<Post | undefined> {
  return (await seriesPosts(series)).find((p) => (p.data as any).role === 'index');
}

/** Human title for any site path that a guide can point at. */
export async function titleForPath(path: string): Promise<string> {
  const [, kind, slug] = path.split('/');
  const map: Record<string, 'posts' | 'stacks' | 'compounds' | 'comparisons'> = { blog: 'posts', stacks: 'stacks', compounds: 'compounds', compare: 'comparisons' };
  const coll = map[kind];
  if (!coll) return path;
  const e = (await records(coll)).find((r) => r.data.slug === slug);
  const d = e?.data as any;
  return d?.short_title || d?.title || d?.preferred_name || slug;
}

/** Breadcrumb trail, root first, ending with the page itself. */
export async function crumbsFor(post: Post): Promise<Crumb[]> {
  const out: Crumb[] = [{ name: 'Home', path: '/' }, { name: 'Guides', path: '/blog' }];
  const chain: Crumb[] = [];
  let parent = (post.data as any).parent as string | undefined;
  let guard = 0;
  while (parent && guard++ < 6) {
    chain.unshift({ name: await titleForPath(parent), path: parent });
    const [, kind, slug] = parent.split('/');
    if (kind !== 'blog') {
      // A programmatic pillar: its own parent is the series index.
      const idx = await indexFor((post.data as any).series);
      if (idx && idx.data.slug !== post.data.slug) chain.unshift({ name: (idx.data as any).short_title || idx.data.title, path: postPath(idx.data.slug) });
      break;
    }
    const p = (await records('posts')).find((r) => r.data.slug === slug);
    parent = (p?.data as any)?.parent;
  }
  const self = { name: (post.data as any).short_title || post.data.title, path: postPath(post.data.slug) };
  return [...out, ...chain, self];
}

/** Turn [[n]] markers into superscript links to sources[n-1]. */
export function cite(html: string, sources: Array<{ id: string; title: string; url: string }>): string {
  return html.replace(/\[\[(\d+)\]\]/g, (m, n) => {
    const s = sources[Number(n) - 1];
    if (!s) return m;
    const t = s.title.replace(/"/g, '&quot;');
    return `<sup class="cite"><a href="${s.url}" target="_blank" rel="nofollow noopener" title="Source ${n}: ${t}" aria-label="Source ${n}">[${n}]</a></sup>`;
  });
}
