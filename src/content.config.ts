// Collections mirror docs/content-contract.md. The Python validator is the
// authoritative cross-record gate in CI; these schemas catch per-record shape
// at build time so a malformed record fails the deploy, not the reader.
import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

export const STATUSES = ['discovered', 'researched', 'draft', 'reviewed', 'published', 'stale', 'retired'] as const;
export const EVIDENCE_LABELS = [
  'approved-label',
  'human-clinical-trial',
  'observational-human',
  'animal-preclinical',
  'mechanistic-in-vitro',
  'community-reported',
  'editorial',
] as const;

const status = z.enum(STATUSES);
const evidenceLabel = z.enum(EVIDENCE_LABELS);

const claim = z.object({
  value: z.string(),
  evidence_label: evidenceLabel,
  source_ids: z.array(z.string()),
  // Verbatim passage the value paraphrases; required by agent/AGENT.md for
  // agent-drafted claims and checked by the reviewer against the source.
  source_excerpt: z.string().optional(),
}).passthrough();

const source = z.object({
  id: z.string(),
  title: z.string(),
  url: z.string().url(),
  published: z.string(),
  kind: z.string().optional(),
}).passthrough();

const review = z.object({
  author: z.string().default(''),
  reviewer: z.string().default(''),
  reviewer_credential: z.string().default(''),
  reviewed_at: z.string().default(''),
}).passthrough();

const changelogEntry = z.object({ date: z.string(), change: z.string() });

const seo = z.object({
  title: z.string().max(60),
  description: z.string().max(160),
}).partial();

// Fields every programmatic record shares.
const base = {
  slug: z.string().regex(/^[a-z0-9]+(?:-[a-z0-9]+)*$/),
  status,
  summary: z.string(),
  seo: seo.optional(),
  attributes: z.record(z.array(claim)).default({}),
  sources: z.array(source).default([]),
  related: z.array(z.string()).default([]),
  faq: z.array(z.object({ question: z.string(), answer: z.string() }).passthrough()).default([]),
  open_questions: z.array(z.string()).default([]),
  review: review.default({}),
  changelog: z.array(changelogEntry).default([]),
  uniqueness_pct: z.number().nullable().optional(),
};

const compounds = defineCollection({
  loader: glob({ pattern: '*.json', base: './data/compounds' }),
  schema: z.object({
    type: z.literal('compound'),
    preferred_name: z.string(),
    aliases: z.array(z.string()).default([]),
    evidence_tier: evidenceLabel,
    comparison_peers: z.array(z.string()).default([]),
    media: z.object({ walkthrough_video: z.string().default(''), transcript: z.string().default('') }).partial().optional(),
    evidence_summary: z.any().optional(),
    ...base,
  }).passthrough(),
});

const stacks = defineCollection({
  loader: glob({ pattern: '*.json', base: './data/stacks' }),
  schema: z.object({
    type: z.literal('stack'),
    title: z.string(),
    components: z.array(z.string()).min(2),
    ...base,
  }).passthrough(),
});

const comparisons = defineCollection({
  loader: glob({ pattern: '*.json', base: './data/comparisons' }),
  schema: z.object({
    type: z.literal('comparison'),
    title: z.string(),
    sides: z.array(z.string()).length(2).optional(),
    ...base,
  }).passthrough(),
});

const tools = defineCollection({
  loader: glob({ pattern: '*.json', base: './data/tools' }),
  schema: z.object({
    type: z.literal('tool'),
    title: z.string(),
    formula: z.string(),
    ...base,
  }).passthrough(),
});

const posts = defineCollection({
  loader: glob({ pattern: '*.json', base: './data/posts' }),
  schema: z.object({
    type: z.literal('post'),
    title: z.string(),
    category: z.string(),
    excerpt: z.string(),
    body: z.string(),
    ...base,
  }).passthrough(),
});

export const collections = { compounds, stacks, comparisons, tools, posts };
