// Runs the calculator scripts exactly as the built pages ship them.
//
//     npm run build && node scripts/test_calculators.mjs
//
// The unit converter and the vial planner shipped for weeks as a heading and a
// paragraph with no calculator at all, and nothing in the build noticed,
// because a page with no form still builds, still validates and still passes a
// link check. This extracts the inline module from each built page, runs it
// against a stub DOM and asserts on what it writes into the output element.
import fs from 'node:fs';
import path from 'node:path';

const DIST = path.resolve(import.meta.dirname, '..', 'dist');
const read = (slug) => {
  const file = path.join(DIST, 'tools', slug, 'index.html');
  if (!fs.existsSync(file)) throw new Error(`${slug}: page not built`);
  const html = fs.readFileSync(file, 'utf8');
  if (!/<form\b/i.test(html)) throw new Error(`${slug}: built page has no <form>`);
  if (!/<output\b/i.test(html)) throw new Error(`${slug}: built page has no <output>`);
  const m = html.match(/<script type="module">([\s\S]*?)<\/script>/i);
  if (!m) throw new Error(`${slug}: built page has no inline module script`);
  return m[1];
};

function render(slug, values, outId) {
  const els = {};
  for (const [id, v] of Object.entries(values)) els[id] = { value: String(v), addEventListener() {} };
  const out = { textContent: '' };
  els[outId] = out;
  globalThis.document = { getElementById: (id) => els[id] ?? null };
  new Function(read(slug))();
  return out.textContent;
}

let pass = 0;
const fails = [];
function check(label, got, want) {
  if (got.includes(want)) { pass++; return; }
  fails.push(`${label}\n     expected to contain: ${want}\n     got:                 ${got}`);
}

const R = 'reconstitution-calculator', C = 'unit-converter', V = 'vial-planner';

// 5 mg in 2 mL is 2500 mcg/mL, so 250 mcg is 0.1 mL.
check('recon: concentration',
  render(R, { 'r-mass': 5, 'r-vol': 2, 'r-want': 250, 'r-scale': 100 }, 'r-out'), '2,500 mcg/mL');
check('recon: U-100 units',
  render(R, { 'r-mass': 5, 'r-vol': 2, 'r-want': 250, 'r-scale': 100 }, 'r-out'), '10 units on a U-100');
// The same volume on a 40-unit scale is 4 units, not 10. Getting this backwards
// is a two-and-a-half-fold error and the page's worked example once said 20.
check('recon: U-40 units',
  render(R, { 'r-mass': 5, 'r-vol': 2, 'r-want': 250, 'r-scale': 40 }, 'r-out'), '4 units on a U-40');
check('recon: whole draws',
  render(R, { 'r-mass': 5, 'r-vol': 2, 'r-want': 250, 'r-scale': 100 }, 'r-out'), 'Whole draws per vial: 20');
check('recon: draw over 1 mL warns',
  render(R, { 'r-mass': 1, 'r-vol': 10, 'r-want': 900, 'r-scale': 100 }, 'r-out'), 'exceeds a 1 mL syringe');
// 10 mg in 1 mL is 10,000 mcg/mL, so 5 mcg is 0.0005 mL: five hundredths of a
// unit, which no syringe barrel is marked for.
check('recon: sub-graduation warns',
  render(R, { 'r-mass': 10, 'r-vol': 1, 'r-want': 5, 'r-scale': 100 }, 'r-out'), 'below the smallest graduation');
check('recon: empty input guarded',
  render(R, { 'r-mass': '', 'r-vol': 2, 'r-want': 250, 'r-scale': 100 }, 'r-out'), 'Enter a positive');

check('convert: mcg to mg',
  render(C, { 'c-amount': 250, 'c-from': 'mcg', 'c-scale': 100 }, 'c-out'), '0.25 mg');
check('convert: mcg to ng',
  render(C, { 'c-amount': 250, 'c-from': 'mcg', 'c-scale': 100 }, 'c-out'), '250,000 ng');
check('convert: mg to mcg',
  render(C, { 'c-amount': 2.5, 'c-from': 'mg', 'c-scale': 100 }, 'c-out'), '2,500 mcg');
check('convert: mL to U-100 units',
  render(C, { 'c-amount': 0.5, 'c-from': 'ml', 'c-scale': 100 }, 'c-out'), '50 units on a U-100');
check('convert: mL to U-40 units',
  render(C, { 'c-amount': 0.5, 'c-from': 'ml', 'c-scale': 40 }, 'c-out'), '20 units on a U-40');

// 10 mg at 300 mcg is 33.33 draws, which is 33 whole draws and 100 mcg stranded.
check('vial: whole draws rounds down',
  render(V, { 'v-mass': 10, 'v-vol': 2, 'v-want': 300, 'v-freq': 3 }, 'v-out'), 'Whole draws per vial: 33');
check('vial: remainder reported',
  render(V, { 'v-mass': 10, 'v-vol': 2, 'v-want': 300, 'v-freq': 3 }, 'v-out'), 'Left in the vial: 100 mcg');
check('vial: duration',
  render(V, { 'v-mass': 10, 'v-vol': 2, 'v-want': 300, 'v-freq': 3 }, 'v-out'), '11 weeks');
check('vial: works without a volume',
  render(V, { 'v-mass': 5, 'v-vol': 0, 'v-want': 250, 'v-freq': 0 }, 'v-out'), 'Whole draws per vial: 20');
check('vial: empty input guarded',
  render(V, { 'v-mass': '', 'v-vol': 2, 'v-want': 250, 'v-freq': 7 }, 'v-out'), 'Enter a positive');

if (fails.length) {
  console.error(`calculator tests: ${pass} passed, ${fails.length} FAILED\n`);
  for (const f of fails) console.error(`  ${f}\n`);
  process.exit(1);
}
console.log(`calculator tests: ${pass} passed`);
