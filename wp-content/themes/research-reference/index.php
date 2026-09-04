<?php
/**
 * Generic fallback: archives, search, blog index, and anything without a
 * more specific template.
 */
get_header();

if (have_posts()) :
    while (have_posts()) :
        the_post();
        ?>
        <article <?php post_class('entry-card'); ?>>
            <h2><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h2>
            <?php the_excerpt(); ?>
        </article>
        <?php
    endwhile;
    the_posts_pagination();
else :
    ?>
    <p>Nothing published here yet.</p>
    <?php
endif;

get_footer();
