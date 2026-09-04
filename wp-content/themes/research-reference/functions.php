<?php
/**
 * Research Reference theme setup.
 */

declare(strict_types=1);

if (!defined('ABSPATH')) {
    exit;
}

function research_reference_setup(): void
{
    add_theme_support('title-tag');
    add_theme_support('post-thumbnails');
    add_theme_support('html5', ['search-form', 'gallery', 'caption', 'style', 'script']);
    add_theme_support('responsive-embeds');
    add_theme_support('editor-styles');
    // Let Elementor Pro replace the header and footer on marketing pages.
    add_theme_support('elementor-header-footer');
    register_nav_menus(['primary' => 'Primary menu']);
}
add_action('after_setup_theme', 'research_reference_setup');

function research_reference_assets(): void
{
    $theme = wp_get_theme();
    wp_enqueue_style('research-reference', get_stylesheet_uri(), [], $theme->get('Version'));
}
add_action('wp_enqueue_scripts', 'research_reference_assets');

/**
 * Read one record meta value, or return the default.
 */
function research_reference_meta(string $key, string $default = ''): string
{
    $value = get_post_meta(get_the_ID(), $key, true);
    return is_string($value) && $value !== '' ? $value : $default;
}
