import matplotlib.pyplot as plt
import matplotlib.patches as patches 
from rectangle import Rectangle
from circle import Circle


class Shape2DPlotter(Rectangle, Circle):
    """
    The Shape2DPlotter class, which inheriths from the Rectangle and Circle class.     

    Methods: 
    - plot(shapes): Defines the shape 2D shape that will be plotted and it's atttributes (example: width, height,x, y ,color,). 
    Adds the shapes to the plotting and sets titel. 
    Plotts it. 

    Example usage for Shape2DPlotter: 
    >>> r1 = Rectangle(x = 100, y = 200, height = 200, width = 100)
    >>> r2 = Rectangle(x = 400, y = 300, height = 100, width = 40)
    >>> r3 = Rectangle(x = 60, y = 100, height = 40, width = 300)
    >>> plotter = Shape2DPlotter()
    >>> plotter.plot([r1, r2, r3])
    Prints the graph with the 3 different shapes on it. 

    """ 
    def __init__(self): 
        """
        Initialize a Shape2DPlotter instance
        
        Arguments:
        - Self 
        """
        pass 


    def plot(self, shapes):
        """
        Takes the shape as an argument and loops the shapes. 
        Defines if its a Rectangle or a Cricle and adds it to the list. 
        Sets attributes from the Rectangle and Circle class with it's given instances. 
        Sets x and y axes and labels and titel.
        """
        fig, ax = plt.subplots()

        for shape in shapes: 
         

            if isinstance(shape, Rectangle): 
                rect_patch = patches.Rectangle(
                    (shape.x, shape.y),
                    shape.width,
                    shape.height,
                    alpha = 0.5, 
                    color = 'yellow'
                )
                ax.add_patch(rect_patch)

            
            elif isinstance(shape, Circle): 
                cir_patch = patches.Circle(
                    (shape.x, shape.y), 
                    shape.radius,  
                    alpha = 0.5,
                    color = 'red'
                    
                )
                ax.add_patch(cir_patch)

        ax.set_xlim(0, 500)
        ax.set_ylim(0, 500)
        ax.set_aspect('equal')
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        plt.title("2D Geometry Plotter")
        plt.show()

