<?php
/**
 * Plugin Name: Research Database
 * Plugin URI:  https://github.com/fosterwei/peptide-research-reference
 * Description: Research-reference content types, record-state index controls, and REST-exposed record fields.
 * Version:     0.2.0
 * Author:      fosterwei
 * License:     GPL-2.0-or-later
 * Requires at least: 6.4
 * Requires PHP: 8.2
 * Text Domain: research-database
 */

declare(strict_types=1);

if (!defined('ABSPATH')) {
    exit;
}

/**
 * Record lifecycle states. Mirrors STATUSES in scripts/validate_content.py
 * and docs/content-contract.md. Only PUBLISHED_STATE is indexable.
 */
const RESEARCH_DB_STATES = [
    'discovered',
    'researched',
    'draft',
    'reviewed',
    'published',
    'stale',
    'retired',
];
const RESEARCH_DB_PUBLISHED_STATE = 'published';

/**
 * Evidence labels. Mirrors EVIDENCE_LABELS in scripts/validate_content.py.
 */
const RESEARCH_DB_EVIDENCE_LABELS = [
    'approved-label',
    'human-clinical-trial',
    'observational-human',
    'animal-preclinical',
    'mechanistic-in-vitro',
    'community-reported',
];

/**
 * Post type key => [plural label, singular label, URL slug].
 * URL slugs mirror docs/content-contract.md.
 */
function research_db_post_types(): array
{
    return [
        'compound'   => ['Compounds',   'Compound',   'compounds'],
        'stack'      => ['Stacks',      'Stack',      'stacks'],
        'comparison' => ['Comparisons', 'Comparison', 'compare'],
        'cycle'      => ['Cycles',      'Cycle',      'cycles'],
        'tool'       => ['Tools',       'Tool',       'tools'],
    ];
}

function research_db_post_type_keys(): array
{
    return array_keys(research_db_post_types());
}

/**
 * Register one public, REST-enabled post type per programmatic page type.
 */
function research_db_register_post_types(): void
{
    foreach (research_db_post_types() as $key => [$plural, $singular, $slug]) {
        register_post_type($key, [
            'labels' => [
                'name'          => $plural,
                'singular_name' => $singular,
                'add_new_item'  => sprintf('Add New %s', $singular),
                'edit_item'     => sprintf('Edit %s', $singular),
                'all_items'     => sprintf('All %s', $plural),
            ],
            'public'        => true,
            'has_archive'   => $slug,
            'rewrite'       => ['slug' => $slug, 'with_front' => false],
            'menu_icon'     => 'dashicons-analytics',
            'supports'      => ['title', 'editor', 'excerpt', 'author', 'revisions', 'custom-fields'],
            'show_in_rest'  => true,
            'rest_base'     => $slug,
        ]);
    }
}
add_action('init', 'research_db_register_post_types');

/**
 * Register the record fields so a REST importer can populate them and
 * templates can read them. Field names mirror the JSON records under data/.
 */
function research_db_register_meta(): void
{
    $string = fn(string $description, string $default = '') => [
        'type'              => 'string',
        'single'            => true,
        'default'           => $default,
        'description'       => $description,
        'show_in_rest'      => true,
        'sanitize_callback' => 'sanitize_text_field',
        'auth_callback'     => fn() => current_user_can('edit_posts'),
    ];

    $json_list = fn(string $description, array $item_schema) => [
        'type'         => 'array',
        'single'       => true,
        'default'      => [],
        'description'  => $description,
        'show_in_rest' => ['schema' => ['type' => 'array', 'items' => $item_schema]],
        'auth_callback' => fn() => current_user_can('edit_posts'),
    ];

    $source_schema = [
        'type'       => 'object',
        'properties' => [
            'id'        => ['type' => 'string'],
            'title'     => ['type' => 'string'],
            'url'       => ['type' => 'string', 'format' => 'uri'],
            'published' => ['type' => 'string'],
            'kind'      => ['type' => 'string'],
        ],
    ];

    foreach (research_db_post_type_keys() as $type) {
        register_post_meta($type, 'record_status', $string('Record lifecycle state', 'draft'));
        register_post_meta($type, 'record_slug', $string('Slug of the source JSON record'));
        register_post_meta($type, 'evidence_tier', $string('Overall evidence label'));
        register_post_meta($type, 'review_author', $string('Named author'));
        register_post_meta($type, 'review_reviewer', $string('Named human reviewer'));
        register_post_meta($type, 'reviewed_at', $string('Review date, YYYY-MM-DD'));
        register_post_meta($type, 'sources', $json_list('Source ledger', $source_schema));
        register_post_meta($type, 'attributes_json', $string('Per-claim attributes with evidence labels and source ids, JSON-encoded'));
    }
}
add_action('init', 'research_db_register_meta');

/**
 * A record is indexable only when WordPress has published it AND the record
 * itself has reached the published lifecycle state.
 */
function research_db_is_indexable(int $post_id): bool
{
    if (get_post_status($post_id) !== 'publish') {
        return false;
    }
    $state = (string) get_post_meta($post_id, 'record_status', true);
    return $state === RESEARCH_DB_PUBLISHED_STATE;
}

/**
 * Emit noindex for any research record that is not indexable.
 */
function research_db_robots(array $robots): array
{
    if (is_singular(research_db_post_type_keys()) && !research_db_is_indexable(get_queried_object_id())) {
        $robots['noindex'] = true;
        $robots['nofollow'] = false;
        unset($robots['max-image-preview']);
    }
    return $robots;
}
add_filter('wp_robots', 'research_db_robots');

/**
 * Keep non-published records out of the core XML sitemap.
 */
function research_db_sitemap_query_args(array $args, string $post_type): array
{
    if (!in_array($post_type, research_db_post_type_keys(), true)) {
        return $args;
    }
    $args['meta_query'] = array_merge($args['meta_query'] ?? [], [[
        'key'   => 'record_status',
        'value' => RESEARCH_DB_PUBLISHED_STATE,
    ]]);
    return $args;
}
add_filter('wp_sitemaps_posts_query_args', 'research_db_sitemap_query_args', 10, 2);

/**
 * Yoast SEO and Rank Math build their own sitemaps. Exclude the same records there.
 */
function research_db_seo_plugin_excluded_ids(array $ids): array
{
    $query = new WP_Query([
        'post_type'      => research_db_post_type_keys(),
        'post_status'    => 'publish',
        'fields'         => 'ids',
        'posts_per_page' => -1,
        'no_found_rows'  => true,
        'meta_query'     => [
            'relation' => 'OR',
            ['key' => 'record_status', 'compare' => 'NOT EXISTS'],
            ['key' => 'record_status', 'value' => RESEARCH_DB_PUBLISHED_STATE, 'compare' => '!='],
        ],
    ]);
    return array_values(array_unique(array_merge($ids, array_map('intval', $query->posts))));
}
add_filter('wpseo_exclude_from_sitemap_by_post_ids', 'research_db_seo_plugin_excluded_ids');
add_filter('rank_math/sitemap/exclude_post_ids', 'research_db_seo_plugin_excluded_ids');

/**
 * Rewrite rules only take effect after a flush. Register types first so the
 * new slugs exist when the flush runs.
 */
function research_db_activate(): void
{
    research_db_register_post_types();
    flush_rewrite_rules();
}
register_activation_hook(__FILE__, 'research_db_activate');
register_deactivation_hook(__FILE__, 'flush_rewrite_rules');
