import type { CollectionEntry } from 'astro:content';

export const SITE_NAME = 'Peptide Research Reference';

export const TIER_LABEL: Record<string, string> = {
  'approved-label': 'Approved label',
  'human-clinical-trial': 'Human clinical trial',
  'observational-human': 'Observational, human',
  'animal-preclinical': 'Animal, preclinical',
  'mechanistic-in-vitro': 'Mechanistic, in vitro',
  'community-reported': 'Community-reported',
};

/** Section headings for compound attribute fields, in template-spec order. */
export const SECTIONS: Array<[field: string, heading: string]> = [
  ['routes_studied', 'Routes studied'],
  ['study_doses', 'Doses reported in studies'],
  ['study_durations', 'Study durations'],
  ['weight_normalized_doses', 'Weight-normalized doses, as published'],
  ['escalation_schedules', 'Escalation schedules used in studies'],
  ['interactions', 'Reported interactions'],
  ['exclusion_criteria', 'Exclusion criteria in studies'],
  ['adverse_events', 'Adverse events and frequency'],
  ['biomarkers_monitored', 'Biomarkers measured in studies'],
  ['reported_timelines', 'Reported timelines'],
  ['storage', 'Storage and stability'],
  ['regulatory_status', 'Regulatory status'],
];

type AnyRecord = CollectionEntry<'compounds' | 'stacks' | 'comparisons' | 'tools' | 'posts'>;

/** Only a fully published record is indexable. Everything else renders noindex. */
export function isIndexable(entry: AnyRecord): boolean {
  return entry.data.status === 'published';
}

/** Last revision date drives <lastmod>; never the build time. */
export function lastmod(entry: AnyRecord): string | undefined {
  const dates = (entry.data.changelog ?? []).map((c) => c.date).filter(Boolean).sort();
  return dates.at(-1);
}

export function title(entry: AnyRecord): string {
  const d = entry.data as { seo?: { title?: string }; preferred_name?: string; title?: string; slug: string };
  return d.seo?.title || d.preferred_name || d.title || d.slug;
}

export function description(entry: AnyRecord): string {
  const d = entry.data as { seo?: { description?: string }; summary?: string; excerpt?: string };
  return d.seo?.description || d.excerpt || d.summary || '';
}

export function formatCount(n: unknown): string {
  return typeof n === 'number' ? n.toLocaleString('en-US') : '—';
}
