from pytest import raises 
from cube import Cube
import math

def test_valid_init(): 
    cube = Cube(side = 5, x =0, y=0) 
    assert cube.side == 5 

def test_area_valid(): 
    cube = Cube(side=2, x = 0, y= 0)
    assert cube.area == (cube.side **2) * 6

def test_perimeter_valid(): 
    cube = Cube(side =3, x = 0, y = 0)
    assert cube.side * 12

def test_volume_valid(): 
    cube = Cube(side =5, x = 0, y = 0)
    assert cube.side ** 3 

def test_negative_side_fail(): 
    with raises(ValueError):
        Cube(side = -1, x = 0, y = 0)

def test_negative_xy_fail(): 
    with raises(ValueError):
        Cube(side = 1, x = -1, y = 0)

def test_type_fail():
    with raises(TypeError): 
        Cube(side = "4", x = True, y=0)

 

    