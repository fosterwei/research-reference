<?php
/**
 * Pages. Elementor takes over the content area when it is active on the page.
 */
get_header();

while (have_posts()) :
    the_post();
    ?>
    <article <?php post_class(); ?>>
        <?php the_content(); ?>
    </article>
    <?php
endwhile;

get_footer();
