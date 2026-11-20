export const DEFAULT_SYRINGE_ML = 1;

/** Capacity and scale are independent: the scale only changes the unit reading. */
export function calculateDraw(vialMg: number, diluentMl: number, massMcg: number, unitsPerMl: number, capacityMl: number) {
  const totalMcg = vialMg * 1000;
  const concentration = totalMcg / diluentMl;
  if (![totalMcg, diluentMl, massMcg, unitsPerMl, capacityMl, concentration].every((n) => Number.isFinite(n) && n > 0)) {
    return { status: 'invalid' } as const;
  }
  if (massMcg > totalMcg) return { status: 'over-vial' } as const;

  const drawMl = (massMcg / totalMcg) * diluentMl;
  const units = drawMl * unitsPerMl;
  if (!Number.isFinite(units) || units <= 0) return { status: 'invalid' } as const;
  return {
    status: drawMl > capacityMl ? 'over-syringe' : 'ok',
    concentration,
    drawMl,
    units,
    draws: Math.floor(totalMcg / massMcg),
  } as const;
}
