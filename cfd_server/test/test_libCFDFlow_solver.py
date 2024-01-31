import PyCFDFlow
import pytest

@pytest.fixture
def my_mesh():
    number_of_cells_in_x = 10 
    number_of_cells_in_y = 10
    dx = 0.1 #[m]
    dy = 0.1 #[m]
    Tw = 10 #[C]
    Te = 10 #[C]
    Tn = 30 #[C]
    Ts = 30 #[C]
    T0 = 0 #[C]

    mesh = PyCFDFlow.Mesh(number_of_cells_in_x, number_of_cells_in_y, dx, dy, Tw, Te, Tn, Ts, T0) 
    
    return mesh



@pytest.mark.parametrize("total_simulation_t", [1, 3, 5, 6, 10])
def test_solver(my_mesh, total_simulation_t):

    my_mesh.set_property("ro", 1)
    my_mesh.set_property("k", 1)
    my_mesh.set_property("cp", 1)
    my_mesh.set_property("Sc", 0)

    solver = PyCFDFlow.Solver(my_mesh)
    
    dt = 0.1
    number_of_time_steps = int(total_simulation_t/dt)

    solver.solve(number_of_time_steps, dt)

    temperature = solver.output_last_temperature()