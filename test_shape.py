from pytest import raises 
from rectangle import Rectangle
from circle import Circle

def test_valid_eq(): 
    circle = Circle(radius=1, x=2, y=2)
    circle2 = Circle(radius=1, x=2, y=2)
    assert circle == circle2

def test_invalid_eq(): 
    c1 = Circle(radius =1, x = 2, y= 2)
    r1 = Rectangle(width=2, height=10, y= 4, x= 2)
    assert c1 != r1

def test_valid_lt(): 
    c1 = Circle(radius=1)
    c2 = Circle(radius=3)
    assert c1.area < c2.area

def test_invalid_lt(): 
    c1 = Circle(radius=4)
    c2 = Circle(radius=2)
    assert not (c1 < c2)

def test_valid_gt(): 
    c1 = Circle(radius=4)
    c2 = Circle(radius=2)
    assert c1 > c2 

def test_invalid_gt(): 
    c1 = Circle(radius=1)
    c2 = Circle(radius=2)
    assert not (c1 > c2)

def test_valid_le(): 
    r1 = Rectangle(width=1, height=2)
    r2 = Rectangle(width=3, height=2)
    assert (r1 <= r2)

def test_valid_ge(): 
    r1 = Rectangle(width=3, height=2) 
    r2 = Rectangle(width=1, height=2)
    assert (r1 >= r2) 

