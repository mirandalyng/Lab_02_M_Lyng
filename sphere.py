import math 
from shape import Shape

class Sphere(Shape):

    def __init__(self, radius:float, x = 0, y = 0): 
        super().__init__(x,y)

        if not all(isinstance(value, (int, float)) for value in (x,y,radius)): 
                raise TypeError(f"Type must be int or float")
            
        if radius < 0: 
            raise ValueError(f"Radius must be a positive number, not {radius}")
            
        if x < 0 or y < 0:
            raise ValueError(f"Values must be positive integers")
            
        self.radius = radius 

    @property
    def area(self): 
        """
        Calculates the surface area of the sphere 
        """
        return 4 * math.pi(self.radius **2)
    
    @property
    def perimeter(self): 
        """
        Calculates the perimeter of the sphere 
        """
        return 2 * math.pi * self.radius 
    
    @property
    def volume(self): 
        """
        Calculates the volume of the sphere 
        """
        return (4/3)* math.pi * (self.radius ** 3)

    def __repr__(self) -> str: 
        """
        A detailed representation to recreate the object in a string 
        """
        return f"{self.__class__.__name__}({self.radius}, x = {self.x}, y = {self.y})"

    def __str__(self) -> str:
        """
        A userfriendly string output of the object in a string
        """ 
        return f"{self.__class__.__name__} with radius: {self.radius}, and positions x = {self.x} and y = {self.y}, area = {self.area:.2f} and perimeter = {self.perimeter:.2f} and volume = {self.volume:.2f}"