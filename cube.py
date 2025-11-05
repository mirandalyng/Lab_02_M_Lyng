from shape import Shape

class Cube(Shape):
    """
        The Cube class, which inheriths from Shape class. 

        Attributes: 
        - side(float): The lenght of each side in the Cube. 
        - x(float): The x-coordinate of the Cube representating center position.
        - y(float): The y-coordinate of the Cube representating center position.

        Example usage for Rectangle: 
        >>> cube = Cube(1,2,3)
        >>> print(cube)
        Cube with side lenght: 1, and positions x = 2 and y = 3, area = 6.00 and perimeter = 12.00 and volume = 1.00 
        
        >>> cube1 = Cube(3)
        >>> cube1
        Cube(side lenght = 3, x = 0, y = 0)

        >>> cube1.translate(2,2)
        >>> cube1
        Cube(side lenght = 3, x = 2, y = 2)

        """ 
    def __init__(self, side: float, x = 0, y = 0):
        """
        Initialize a Cube instance

        Inheritates the x,y from Shape class. 
        
        Arguments:
        side(float): not optional 
        x(float): optional , by default 0 
        y(float): optional , by default 0 

        Raises: 
        TypeError: If any of the arguments is not int or float (x,y,side). 
        ValueError: If any of the arguments (side, x, y) are negative.
        
        """

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
        return f"{self.__class__.__name__}(side lenght = {self.side}, x = {self.x}, y = {self.y})"

    def __str__(self) -> str:
        """
        A userfriendly string output of the object in a string
        """ 
        return f"{self.__class__.__name__} with side lenght: {self.side}, and positions x = {self.x} and y = {self.y}, area = {self.area:.2f} and perimeter = {self.perimeter:.2f} and volume = {self.volume:.2f}"