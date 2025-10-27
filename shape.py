
from abc import ABC, abstractmethod



class Shape(ABC): 
    def __init__(self, x: float, y: float):
        self.x = x 
        self.y = y 


    """Abstract Propertys are defined"""

    @property
    @abstractmethod
    def area(self) -> None: 
        pass 
    """Returnes the area of the shape"""
    

    @property 
    @abstractmethod 
    def perimeter(self) -> None:  
        pass 
    """Returnes the perimeter of the shape"""


    def __eq__(self, other) -> bool:
        if not isinstance(other, Shape): 
            return NotImplemented
        
        return self.area == other.area 
    """Check that the area is the same in self and other 
    ex circle1(self) == circle2(other)"""

    def __lt__(self, other) -> bool: 
        if not isinstance(other,Shape): 
            return NotImplemented
        
        return self.area < other.area
    """Check that the area is less  in self and other 
    ex circle1(self) < circle2(other)"""

    def __gt__(self, other) -> bool: 
        if not isinstance(other, Shape): 
            return NotImplemented 
        
        return self.area > other.area
    """Check that the area is more in self and other 
    ex circle1(self) > circle2(other)"""

    def __le__(self, other) -> bool:
        if not isinstance(other, Shape): 
            return NotImplemented
        
        return self.area <= other.area
    """Check that the area is less or equal in self and other 
    ex circle1(self) <= circle2(other)"""

    def __ge__(self, other) -> bool:
        if not isinstance(other, Shape): 
            return NotImplemented
        
        return self.area >= other.area
    """Check that the area is more or equal in self and other 
    ex circle1(self) >= circle2(other)"""


    def translate(self,dx,dy): 
        if not all(isinstance(value, (int, float)) for value in (dx,dy)): 
            raise TypeError(f"Type must be int or float")

        self.x += dx
        self.y += dy
        
