<?php
/**
 * Shared body for compound, stack, comparison, cycle, and tool pages.
 * Reads the record fields registered by the Research Database plugin.
 */

$status     = research_reference_meta('record_status', 'draft');
$tier       = research_reference_meta('evidence_tier');
$reviewer   = research_reference_meta('review_reviewer');
$reviewed   = research_reference_meta('reviewed_at');
$sources    = get_post_meta(get_the_ID(), 'sources', true);
$attributes = json_decode(research_reference_meta('attributes_json', '{}'), true) ?: [];
?>
<article <?php post_class(); ?>>
    <?php if ($status !== 'published') : ?>
        <p class="record-notice">
            This record is in <strong><?php echo esc_html($status); ?></strong> state. It has not completed human review and is not indexed.
        </p>
    <?php endif; ?>

    <h1><?php the_title(); ?></h1>

    <dl class="record-meta">
        <?php if ($tier) : ?>
            <dt>Evidence</dt><dd><span class="evidence-label"><?php echo esc_html($tier); ?></span></dd>
        <?php endif; ?>
        <?php if ($reviewer) : ?>
            <dt>Reviewed by</dt><dd><?php echo esc_html($reviewer); ?><?php echo $reviewed ? ' on ' . esc_html($reviewed) : ''; ?></dd>
        <?php endif; ?>
    </dl>

    <?php the_content(); ?>

    <?php if (!empty($attributes) && is_array($attributes)) : ?>
        <section class="entry-card">
            <h2>What the research reports</h2>
            <?php foreach ($attributes as $field => $claims) : ?>
                <?php if (!is_array($claims) || $claims === []) { continue; } ?>
                <h3><?php echo esc_html(ucwords(str_replace('_', ' ', (string) $field))); ?></h3>
                <ul>
                    <?php foreach ($claims as $claim) : ?>
                        <li>
                            <?php echo esc_html((string) ($claim['value'] ?? '')); ?>
                            <?php if (!empty($claim['evidence_label'])) : ?>
                                <span class="evidence-label"><?php echo esc_html((string) $claim['evidence_label']); ?></span>
                            <?php endif; ?>
                            <?php if (!empty($claim['source_ids']) && is_array($claim['source_ids'])) : ?>
                                <small>[<?php echo esc_html(implode(', ', array_map('strval', $claim['source_ids']))); ?>]</small>
                            <?php endif; ?>
                        </li>
                    <?php endforeach; ?>
                </ul>
            <?php endforeach; ?>
        </section>
    <?php endif; ?>

    <?php if (is_array($sources) && $sources !== []) : ?>
        <section class="sources">
            <h2>Sources</h2>
            <ol>
                <?php foreach ($sources as $source) : ?>
                    <li id="<?php echo esc_attr((string) ($source['id'] ?? '')); ?>">
                        <a href="<?php echo esc_url((string) ($source['url'] ?? '')); ?>" rel="noopener nofollow" target="_blank">
                            <?php echo esc_html((string) ($source['title'] ?? $source['url'] ?? 'Source')); ?>
                        </a>
                        <?php if (!empty($source['published'])) : ?>
                            (<?php echo esc_html((string) $source['published']); ?>)
                        <?php endif; ?>
                    </li>
                <?php endforeach; ?>
            </ol>
        </section>
    <?php endif; ?>

    <p class="record-meta">Research reference only. Not medical, dosing, or treatment advice.</p>
</article>
