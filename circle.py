
import math 
from shape import Shape 

class Circle(Shape): 
    """
    The Circle class, which inheriths from Shape class. 

    Attributes: 
    - radius(float): The radius of the circle.
    - x(float): The x-coordinate of the circle's center.
    - y(float): The y-coordinate of the circle's center.

    Methods: 
    - is_unit_circle(): Calculates if the radie is 1 in a circle and has the origin (0,0) 
            Return: True / False

    Example usage for Circle: 
    >>> circle1 = Circle(x=0, y=0, radius=1)
    >>> circle1
    Circle(radius = 1, x = 0, y = 0)

    >>> circle1.is_unit_circle() 
    True 
    """ 

    def __init__(self, radius: float, x=0 , y =0 ): 
        """
        Initialize a Circle instance

        Inheritates the x,y from Shape class. 
        
        Arguments:
        radius(float): not optional 
        x(float): optional , by default 0 
        y(float): optional , by default 0 

        Raises: 
        TypeError: If any of the arguments is not int or float (x,y,radius). 
        ValueError: If any of the arguments (radius, x, y) are negative.
        
        """
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
        Calculates the area of the circle
        """
        return math.pi * self.radius **2
    
    @property
    def perimeter(self): 
        """
        Calculates the perimeter of the circle
        """
        return 2 * math.pi * self.radius
    
    def is_unit_circle(self) -> bool: 
        """
        Calculates if the circle is unit or not
        """
        return self.x**2 + self.y**2 <= 1
    
    def __repr__(self) -> str: 
        """
        A detailed representation to recreate the object in a string 
        """
        return f"{self.__class__.__name__}(radius = {self.radius}, x = {self.x}, y = {self.y})"

    def __str__(self) -> str:
        """
        A userfriendly string output of the object in a string
        """ 
        return f"{self.__class__.__name__} with radius: {self.radius}, and positions x = {self.x} and y = {self.y}, area = {self.area:.2f} and perimeter = {self.perimeter:.2f}"