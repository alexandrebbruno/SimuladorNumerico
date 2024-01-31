import reaktoro as rkt
import numpy as np

def simulate(input):
    
    temperature_min = 0# float(input['temperatura_min'])
    temperature_max = 100#float(input['temperatura_max']) 
    pressure = 1#float(input['pressure'])
    cl = 0.19#float(input['cl'])
    na = 0.10#float(input['na'])
    so4 = 0.03#float(input['so4'])
    mg = 0.01#float(input['mg'])
    ca = 0.004#float(input['ca'])
    k = 0.003#float(input['k'])s
    hco3 = 0#float(input['hco3'])
    br = 0.0006#float(input['br'])
    co3 = 0.1#float(input['co3'])
    sr = 0.1#float(input['sr'])

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

    results = {
        'temperatures': temperatures,
        'densities': densities
    }

    return results
