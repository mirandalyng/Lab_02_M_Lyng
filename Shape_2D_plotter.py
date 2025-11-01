import matplotlib.pyplot as plt
import matplotlib.patches as patches 
from rectangle import Rectangle
from circle import Circle

class Shape2DPlotter(Rectangle, Circle):
    
    def __init__(self): 
         
        pass 


    def plot(self, shapes):

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

