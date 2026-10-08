import type { CollectionEntry } from 'astro:content';

// The brand, matching the domain and the wordmark on the social card, with
// the category keyword in it. Length is a real constraint: it is appended to
// every page title that can still fit inside 60 characters, so a longer name
// brands fewer pages. At 17 characters this suffix reaches 16 of 63 pages;
// 'Dashnaiv Peptide Reference' would reach 10.
// Every title suffix, the footer, and the Organization in each page's
// JSON-LD read from here, so the site names itself in exactly one place.
export const SITE_NAME = 'Dashnaiv Peptides';

// Site-wide social card. 1200x630 (1.91:1), the ratio Facebook, LinkedIn,
// Slack, Discord and X all accept, and large enough for the
// max-image-preview:large directive the pages already set. A page may pass its
// own `image` to Base; none does yet, so every card is this one.
// The one published contact route. It appears only in a mailto href, never as
// visible text, which keeps it out of the plain-text scrape that harvests an
// address printed on a page.
export const CONTACT_EMAIL = 'corrections@dashnaiv.com';

// Google Analytics 4. Empty disables the tag entirely, which is how a fork or a
// local build runs without reporting into someone else's property. Changing
// this changes what the privacy page has to say, and scripts/check_links.py
// fails the build if the two stop agreeing.
export const GA_MEASUREMENT_ID = 'G-WNMRQE3MLF';

export const OG_IMAGE = '/og.jpg';

// Bumped when an icon file changes. Browsers cache favicons separately from
// pages and ignore a normal reload, including the absence of one, so the only
// reliable way to move a client onto a new icon is to change the URL.
export const ICON_V = '3';
export const OG_IMAGE_ALT =
  'Laboratory vials beside a molecular model, with the site name and the line "Every claim cited, tiered and dated".';

export const TIER_LABEL: Record<string, string> = {
  'approved-label': 'Approved label',
  'human-clinical-trial': 'Human clinical trial',
  'observational-human': 'Observational, human',
  'animal-preclinical': 'Animal, preclinical',
  'mechanistic-in-vitro': 'Mechanistic, in vitro',
  'community-reported': 'Community-reported',
  'editorial': 'Editorial synthesis',
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

/**
 * A page is indexable when it is actually finished: a written guide, and a
 * named reviewer who signed it. Status alone was the rule before and it does
 * not work, because `status` is set by hand and every record still says
 * 'draft' long after being written and reviewed. That let seven auto-drafted
 * records with no prose and no reviewer into the index, while the homepage and
 * the directory pages, which asked for 'published', stayed out of it. Both
 * failures came from trusting a field nobody updates. These two conditions are
 * things the record either has or does not.
 *
 * Tools and posts carry no guide or review, so they keep the status rule.
 */
export function isIndexable(entry: AnyRecord): boolean {
  if (!['draft', 'reviewed', 'published'].includes(entry.data.status)) return false;
  const d = entry.data as Record<string, any>;
  if (entry.collection === 'tools' || entry.collection === 'posts') return true;
  return Boolean(d.guide?.length) && Boolean(d.review?.reviewer);
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
