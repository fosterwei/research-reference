<?php
/**
 * Editorial posts at /blog/{slug}.
 */
get_header();

while (have_posts()) :
    the_post();
    ?>
    <article <?php post_class(); ?>>
        <h1><?php the_title(); ?></h1>
        <p class="record-meta">
            <?php echo esc_html(get_the_date()); ?> · <?php the_author(); ?>
        </p>
        <?php the_content(); ?>
    </article>
    <?php
endwhile;

get_footer();
