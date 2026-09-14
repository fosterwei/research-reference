// The compound registry: identity, taxonomy and the page plan. Hand-maintained
// in research/registry.json, checked in CI by scripts/build_registry.py.
import registry from '../../research/registry.json';

export type RegistryCompound = (typeof registry.compounds)[number];
export type RegistryStack = (typeof registry.stacks)[number];
export type RegistryComparison = (typeof registry.comparisons)[number];
export type RegistryTool = (typeof registry.tools)[number];

export const classes: Record<string, string> = registry.classes;
export const compounds: RegistryCompound[] = registry.compounds;
export const stacks: RegistryStack[] = registry.stacks;
export const comparisons: RegistryComparison[] = registry.comparisons;
export const tools: RegistryTool[] = registry.tools;

export function compound(slug: string): RegistryCompound | undefined {
  return compounds.find((c) => c.slug === slug);
}

/** Same class, excluding the compound itself. Feeds section 19 and related links. */
export function peers(slug: string): RegistryCompound[] {
  const me = compound(slug);
  if (!me) return [];
  return compounds.filter((c) => c.class === me.class && c.slug !== slug).sort((a, b) => a.slug.localeCompare(b.slug));
}

export function stacksContaining(slug: string): RegistryStack[] {
  return stacks.filter((s) => s.components.includes(slug));
}

export function comparisonsWith(slug: string): RegistryComparison[] {
  return comparisons.filter((c) => c.sides.includes(slug));
}

export function className(id: string): string {
  return id.replace(/-/g, ' ').replace(/\band\b/g, '&');
}
