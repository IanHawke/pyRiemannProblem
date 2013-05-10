from model import Model

traffic = Model(1, lambda q:(q*(1.0-q)), lambda q:(1.0 - 2.0*q), lambda q:-2.0)

from scalar import solve_RP

solution_shock = solve_RP(traffic, 0.1, 0.9)
solution_raref = solve_RP(traffic, 0.9, 0.1)

# solutions_raref.plot_wave([-1.0, 1.0])
