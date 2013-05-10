from model import Model
import sympy

q = sympy.Symbol("q")
f = q*(1-q)
flux    = sympy.lambdify([q], f)
d_flux  = sympy.lambdify([q], sympy.diff(f, q))
dd_flux = sympy.lambdify([q], sympy.diff(f, q, 2))

traffic_symbolic = Model(1, flux, d_flux, dd_flux)

from scalar import solve_RP

solution_shock_symbolic = solve_RP(traffic_symbolic, 0.1, 0.5)
solution_raref_symbolic = solve_RP(traffic_symbolic, 0.9, 0.1)

# solutions_raref_symbolic.plot_wave([-1.0, 1.0])
