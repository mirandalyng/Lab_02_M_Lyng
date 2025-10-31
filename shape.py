from abc import ABC, abstractmethod

class Shape(ABC): 
    """
    Superclass/parentclass representing a Shape. 

    Attributes: 
    - x(float): The shapes posistion on the x-coordinate
    - y(float): The shapes posistion on the y-coordinate

    Methods:
    - __eq__(): Checks if the shape type, area and perimeter is equal in two different instantiations. 
            Returns:  True/False 

    - __lt__(): Checks if one area is less than the other area in two instantiations.
            Return: True/False 
    
    - __gt__(): Checks if one area is greater than the other area in two instantiations.
            Return: True/False 

    -__le__():Checks if one area is less than OR equal to the other area in two instantiations. 
            Return: True/False 

    -__ge__():Checks if one area is greater than OR equal the other area in two instantiations. 
            Return: True/False 

    -translate(): Moves the coordinates by adding the dx coordinate value and dy coordinate value to the exsisting x-coordinate and y-coordinate.  
            Return: The dx-coordinate and the yx-coordinate 
    
    Example usage in subclasses for Shape:  
    
    >>> rectangle =(1,2)
    >>> rectangle2 =(1,2)
    >>> rectangle1 == rectangle2
    True 

    >>> circle1 = Circle(x=0, y=0, radius=1)
    >>> circle1.translate(5, 3) 
    Circle(1, x = 5, y = 3)

    """

    def __init__(self, x: float, y: float):
        self.x = x 
        self.y = y 
        """
        Initializes a new instance of the Shape class
        """

    @property
    @abstractmethod
    def area(self) -> float: 
        """
        Defines property area: abstract
        """
        pass 
  
    @property 
    @abstractmethod 
    def perimeter(self) -> float:  
        """
        Defines property perimeter: abstract
        """
        pass 

    def __eq__(self, other) -> bool:
        if not isinstance(other, Shape): 
            return NotImplemented
        """
        Method containing equal-check on type, area and perimeter 
        """
        return (
            type(self) == type(other) and 
            self.area == other.area and 
            self.perimeter == other.perimeter
            )
    

    def __lt__(self, other) -> bool: 
        if not isinstance(other,Shape): 
            return NotImplemented
        """
        Method containing a less than check using the area on the shape
        """
        return self.area < other.area
   
    def __gt__(self, other) -> bool: 
        if not isinstance(other, Shape): 
            return NotImplemented 
        """
        Method containing a greater than check using the area on the shape
        """
        return self.area > other.area

    def __le__(self, other) -> bool:
        if not isinstance(other, Shape): 
            return NotImplemented
        """
        Method containing a less than OR equal check using the area on the shape
        """
        return self.area <= other.area
 
    def __ge__(self, other) -> bool:
        if not isinstance(other, Shape): 
            return NotImplemented
        """
        Method containing a greater than OR equal check using the area on the shape
        """
        return self.area >= other.area
    
    def translate(self,dx,dy): 
        if not all(isinstance(value, (int, float)) for value in (dx,dy)): 
            raise TypeError(f"Type must be int or float")
        """
        Adding values to the x-coordinate and y-coordinate
        """
        self.x += dx
        self.y += dy

    def __repr__(self) -> str:
        """
        A detailed representation to recreate the object in a string 
        """
        return(f"{self.__class__.__name__}(x = {self.x}, y = {self.y})")
        
    def __str__(self) -> str: 
        """
        A userfriendly string output of the object in a string
        """
        return f"{self.__class__.__name__} with positions (x: {self.x} and y: {self.y})"