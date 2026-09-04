<!doctype html>
<html <?php language_attributes(); ?>>
<head>
    <meta charset="<?php bloginfo('charset'); ?>">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>
<?php if (!function_exists('elementor_theme_do_location') || !elementor_theme_do_location('header')) : ?>
<header class="site-header">
    <a href="<?php echo esc_url(home_url('/')); ?>"><?php bloginfo('name'); ?></a>
    <?php wp_nav_menu(['theme_location' => 'primary', 'container' => 'nav', 'fallback_cb' => false]); ?>
</header>
<?php endif; ?>
<main class="site-main">
