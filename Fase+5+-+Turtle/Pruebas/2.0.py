import turtle
import math

# personalizacion de la ventana
window = turtle.Screen()
window.title("Extendiendo una tortuga")
window.bgcolor("#68a0ed")
window.setup(500, 500)
window.setworldcoordinates(0, 500, 500, 0)


class Tortuga(turtle.Turtle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pensize(2)
        self.shape("turtle")
        self.color("darkgreen")

    def rectangulo(self, x, y, ancho, alto, color="black"):
        self.color(color)
        self.penup()
        self.goto(x-ancho/2, y-alto/2)  # vertice superior izquierda
        self.pendown()
        self.goto(x+ancho/2, y-alto/2)  # vertice superior derecho
        self.goto(x+ancho/2, y+alto/2)  # vertice inferior derecho
        self.goto(x-ancho/2, y+alto/2)  # vertice inferior izquierdo
        self.goto(x-ancho/2, y-alto/2)  # vertice superior izquierdo
