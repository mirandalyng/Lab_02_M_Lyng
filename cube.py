import math 
from shape import Shape

class Cube(Shape):

    def __init__(self, side: float, x = 0, y = 0):
        super().__init__(x, y)

        if not all(isinstance(value, (int, float)) for value in (x,y,side)): 
            raise TypeError(f"Type must be int or float")
        
        if side < 0: 
            raise ValueError(f"The side must be a positive number, not {side}")
        
        if x < 0 or y < 0:
            raise ValueError(f"Values must be positive integers")
        
        self.side = side

    @property
    def area(self): 
        """
        Calculates the surface area of the cube 
        """
        return (self.side **2) * 6
    
    @property
    def perimeter(self): 
        """
        Calculates the perimeter of the cube 
        """
        return self.side * 12 

    @property
    def volume(self): 
        """
        Calculates the volume of the cube 
        """
        return self.side ** 3


    def __repr__(self) -> str: 
        """
        A detailed representation to recreate the object in a string 
        """
        return f"{self.__class__.__name__}({self.side}, x = {self.x}, y = {self.y})"

    def __str__(self) -> str:
        """
        A userfriendly string output of the object in a string
        """ 
        return f"{self.__class__.__name__} with side lenght: {self.side}, and positions x = {self.x} and y = {self.y}, area = {self.area:.2f} and perimeter = {self.perimeter:.2f} and volume = {self.volume:.2f}"