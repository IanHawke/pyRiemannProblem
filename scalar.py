from model import Model
from wave import Wave
import numpy as np
from scipy import optimize

def solve_RP(model, left, right):
    """Solve the Riemann problem for a general scalar flux"""

    # Note that for now it only does the convex case

    assert(model.convex)

    lambda_l = model.d_flux(left)
    lambda_r = model.d_flux(right)
    flux_l = model.flux(left)
    flux_r = model.flux(right)

    # Convex or concave?
    if (model.dd_flux(left) > 0.0):
        convex_sign = 1.0
    else:
        convex_sign =-1.0

    if (lambda_l > lambda_r):
        # Shock wave
        v_s = (flux_r - flux_l) / (right - left)
        wave_start = v_s
        wave_end   = v_s
        solution = Wave(model, wave_start, wave_end, left, right)
    else:
        # Rarefaction wave
        wave_start = lambda_l
        wave_end   = lambda_r
        xi = np.linspace(wave_start, wave_end)
        raref = np.zeros_like(xi)
        for i in range(len(xi)):
            raref[i] = optimize.brentq(lambda q:model.d_flux(q) - xi[i], left, right)
        solution = Wave(model, wave_start, wave_end, left, right, xi, raref)

    return solution

