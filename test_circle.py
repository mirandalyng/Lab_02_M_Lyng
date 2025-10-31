from pytest import raises 
from circle import Circle
import math

def test_valid_init(): 
    circle = Circle(radius = 5, x =0, y=0) 
    assert circle.radius == 5 

def test_area_valid(): 
    c1 = Circle(radius=2, x = 0, y= 0)
    assert c1.area == math.pi * c1.radius **2

def test_perimeter_valid(): 
    c1 = Circle(radius=2, x = 0, y = 0)
    assert c1.perimeter == 2 * math.pi * c1.radius

def test_unit_circle_valid(): 
    c1 = Circle(radius=1, y=0, x=0)
    assert c1.is_unit_circle() is True

def test_negative_radius_fail(): 
    with raises(ValueError):
        Circle(radius = -1, x = 0, y = 0)

def test_negative_xy_fail(): 
    with raises(ValueError):
        Circle(radius = 1, x = -1, y = 0)

def test_type_fail():
    with raises(TypeError): 
        Circle(radius = "4", x = True, y=0)

 

    