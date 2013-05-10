from model import Model
import sympy

q = sympy.Symbol("q")
f = q**2/2
flux    = sympy.lambdify([q], f)
d_flux  = sympy.lambdify([q], sympy.diff(f, q))
dd_flux = sympy.lambdify([q], sympy.diff(f, q, 2))

burgers_symbolic = Model(1, flux, d_flux, dd_flux)

from scalar import solve_RP

solution_shock_symbolic = solve_RP(burgers_symbolic, 2.0, 1.0)
solution_raref_symbolic = solve_RP(burgers_symbolic, 1.0, 2.0)

# solutions_raref_symbolic.plot_wave([0.0, 5.0])
