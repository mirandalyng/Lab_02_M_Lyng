import math
from abc import ABC, abstractmethod



class Shape: 
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


    


    def __eq__(self, other) -> Bool: 

    def __lt__(self, other) -> Bool: 

    def __gt__(self, other) -> Bool: 

    def __le__(self, other) -> Bool:
    
    def __ge__(self, other) -> Bool:



