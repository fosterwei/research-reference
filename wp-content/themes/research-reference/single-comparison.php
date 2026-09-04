<?php
/**
 * Comparison page. Shares the research-record body with the other programmatic types.
 */
get_header();

while (have_posts()) :
    the_post();
    get_template_part('template-parts/research-record');
endwhile;

get_footer();
