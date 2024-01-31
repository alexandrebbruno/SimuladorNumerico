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

@pytest.mark.parametrize("ro", [7750, 1000, 1500, 3000, 5000])
def test_set_ro_properties(my_mesh, ro):

    my_mesh.set_property("ro", ro)

@pytest.mark.parametrize("cp", [420, 300, 150, 320, 500])
def test_set_cp_properties(my_mesh, cp):

    my_mesh.set_property("cp", cp)


@pytest.mark.parametrize("k", [71, 30, 45, 80, 75])
def test_set_k_properties(my_mesh, k):

    my_mesh.set_property("k", k)