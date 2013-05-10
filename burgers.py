from model import Model

burgers = Model(1, lambda q:(q**2)/2.0, lambda q:q, lambda q:1.0)

from scalar import solve_RP

solution_shock = solve_RP(burgers, 2.0, 1.0)
solution_raref = solve_RP(burgers, 1.0, 2.0)

# solutions_raref.plot_wave([0.0, 5.0])
