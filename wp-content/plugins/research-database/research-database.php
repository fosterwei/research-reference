<?php
/**
 * Plugin Name: Research Database
 * Description: Safe-by-default content types and index controls.
 * Version: 0.1.0
 */
if (!defined('ABSPATH')) exit;
add_action('init', function () {
  register_post_type('compound', ['label'=>'Compounds','public'=>true,'has_archive'=>'protocols','rewrite'=>['slug'=>'protocols'],'supports'=>['title','editor','excerpt','author','revisions'],'show_in_rest'=>true]);
  register_post_type('stack', ['label'=>'Stacks','public'=>true,'has_archive'=>'stacks','rewrite'=>['slug'=>'stacks'],'supports'=>['title','editor','excerpt','author','revisions'],'show_in_rest'=>true]);
  register_post_type('comparison', ['label'=>'Comparisons','public'=>true,'has_archive'=>'compare','rewrite'=>['slug'=>'compare'],'supports'=>['title','editor','excerpt','author','revisions'],'show_in_rest'=>true]);
});
add_filter('wp_robots', function ($robots) {
  if (is_singular(['compound','stack','comparison']) && get_post_status() !== 'publish') $robots['noindex'] = true;
  return $robots;
});
