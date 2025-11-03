from pytest import raises 
from sphere import Sphere
import math

def test_valid_init(): 
    sp1 = Sphere(radius = 5, x =0, y=0) 
    assert sp1.radius == 5 

def test_area_valid(): 
    sp1 = Sphere(radius=2, x = 0, y= 0) 
    assert sp1.area == 4 * math.pi * (sp1.radius ** 2)

def test_perimeter_valid(): 
    sp = Sphere(radius= 3, x = 0, y = 0)
    assert 2 * math.pi * sp.radius 

def test_volume_valid(): 
    sp = Sphere(radius = 5, x = 0, y = 0)
    assert (4/3) * math.pi * (sp.radius ** 3)

def test_negative_radius_fail(): 
    with raises(ValueError):
        Sphere(radius= -1, x = 0, y = 0)

def test_negative_xy_fail(): 
    with raises(ValueError):
        Sphere(radius = 1, x = -1, y = 0)

def test_type_fail():
    with raises(TypeError): 
        Sphere(radius= "4", x = True, y=0)

 

    