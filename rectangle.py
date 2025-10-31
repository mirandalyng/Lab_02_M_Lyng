import math 
from shape import Shape 

class Rectangle(Shape): 
    """
        The Rectangle class, which inheriths from Shape class. 

        Attributes: 
        - width(float): The width of the rectangle.
        - height(float): The height of the rectangle.
        - x(float): The x-coordinate of the rectangle representating center position.
        - y(float): The y-coordinate of the rectangle representating center position.

        Methods: 
        - is_unit_square(): Calculates if the rectangle is a square or not. 
                Return: True / False

        Propertys: 
        - area{}: inherits an abstract property/method and calculates the area of the rectangle
        - perimeter{}: inherits an abstract property/method and calculates the perimeter of the rectangle


        """ 

    def __init__(self, width:float, height:float, x = 0, y = 0):
        """
        Initialize a Rectangle instance

        Inheritates the x,y from Shape class. 
        
        Arguments:
        width(float): not optional 
        height(float): not optional 
        x(float): optional , by default 0 
        y(float): optional , by default 0 

        Raises: 
        TypeError: If any of the arguments is not int or float (x,y,width, height). 
        ValueError: If width or height are negative integers. 
        
        """
        super().__init__(x,y)

        if not all(isinstance(value, (int, float)) for value in (x,y,width,height)): 
            raise TypeError(f"Type must be int or float")
        
        if width <= 0 or height <= 0:  
            raise ValueError(f"Width and height need to be positive values")
        
        self.width = width 
        self.height = height
    
    @property
    def area(self): 
        """
        Calculates the area of the rectangle
        """
        return self.width * self.height
    
    @property
    def perimeter(self):
        """
        Calculates the perimeter of the rectangle
        """ 
        return 2*(self.width + self.height)

    def is_unit_square(self) -> bool:
        """
        Calculates if the rec is square or not 
        """
        return self.width == self.height
     
    def __repr__(self) -> str: 
        """
        A detailed representation to recreate the object in a string 
        """
        return f"{self.__class__.__name__}(width = {self.width}, height = {self.height}, x = {self.x}, y = {self.y})"

    def __str__(self) -> str: 
        """
        A userfriendly string output of the object in a string
        """ 
        return f"{self.__class__.__name__} with width = {self.width}, height= {self.height}= {self.x} and y = {self.y}, area = {self.area:.2f} and perimeter = {self.perimeter:.2f}"
