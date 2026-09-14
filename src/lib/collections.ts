// getCollection() warns loudly when a collection has no entries, and four of
// ours are empty until their first record lands. Check the folder first so
// deploy logs stay readable.
import { getCollection, type CollectionEntry, type CollectionKey } from 'astro:content';

const FILES: Record<CollectionKey, Record<string, unknown>> = {
  compounds: import.meta.glob('/data/compounds/*.json'),
  stacks: import.meta.glob('/data/stacks/*.json'),
  comparisons: import.meta.glob('/data/comparisons/*.json'),
  tools: import.meta.glob('/data/tools/*.json'),
  posts: import.meta.glob('/data/posts/*.json'),
};

export async function records<K extends CollectionKey>(name: K): Promise<CollectionEntry<K>[]> {
  if (Object.keys(FILES[name]).length === 0) return [];
  return getCollection(name);
}
