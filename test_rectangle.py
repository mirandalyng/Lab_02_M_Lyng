from pytest import raises 
from rectangle import Rectangle

def test_valid_init(): 
    rec = Rectangle(width= 4, height = 5, x =0, y=0) 
    assert rec.width == 4 and rec.height == 5 

def test_area_valid(): 
    r1 = Rectangle(width=3, height = 2, x = 0, y= 0)
    assert r1.area == r1.width * r1.height

def test_perimeter_valid(): 
    r1 = Rectangle(width = 3, height=2, x = 0, y = 0)
    assert r1.perimeter == 2 * (r1.width + r1.height)

def test_unit_square_valid(): 
    r1 = Rectangle(width = 2, height = 2, y=0, x=0)
    assert r1.is_unit_square() is True

def test_negative_height_fail(): 
    with raises(ValueError):
        Rectangle(width = 1 , height = -1, x = 0, y = 0)

def test_negative_width_fail(): 
    with raises(ValueError):
        Rectangle(width = -1 , height = 1, x = 0, y = 0)

def test_negative_xy_fail(): 
    with raises(ValueError):
        Rectangle(width = 2, height = 1, x = -1, y = 0)

def test_type_fail():
    with raises(TypeError): 
        Rectangle(width = "4", height = 2, x = True, y=0)
