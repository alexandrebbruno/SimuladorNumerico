import reaktoro as rkt
import numpy as np

def test_simulador_calculo_temperatura():
    
    temperature_min = 0
    temperature_max = 100
    pressure = 1
    cl = 0.19
    na = 0.10
    so4 = 0.03
    mg = 0.01
    ca = 0.004
    k = 0.003
    hco3 = 0
    br = 0.0006
    co3 = 0.1
    sr = 0.1

    db = rkt.PhreeqcDatabase("pitzer.dat")

    solution = rkt.AqueousPhase("H2O Cl- Na+ SO4-2 Mg+2 Ca+2 K+ HCO3- Br- CO3-2 Sr+2")
    solution.set(rkt.ActivityModelPitzer())

    system = rkt.ChemicalSystem(db, solution)

    state = rkt.ChemicalState(system)
    state.pressure(pressure, "atm")
    state.set("H2O", 1.0, "kg")
    state.set("Cl-", cl, "kg")
    state.set("Na+", na, "kg")
    state.set("SO4-2", so4, "kg")
    state.set("Mg+2", mg, "kg")
    state.set("Ca+2", ca, "kg")
    state.set("K+", k, "kg")
    state.set("HCO3-", hco3, "kg")
    state.set("Br-", br, "kg")
    state.set("CO3-2", co3, "kg")
    state.set("Sr+2", sr, "kg")

    solver = rkt.EquilibriumSolver(system)

    temperatures_np = np.arange(temperature_min, temperature_max, 0.3)
    densities = []
    temperatures = []

    for i in range(len(temperatures_np)):
        state.temperature(temperatures_np[i], "celsius")
        solver.solve(state)
        density = rkt.ChemicalProps(state).density().val()
        densities.append(density)
        temperatures.append(temperatures_np[i])
