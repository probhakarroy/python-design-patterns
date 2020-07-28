class DrawingAPIOne:
    """Implementation-specific abstraction: concrete class one"""

    def draw_circle(self, x, y, radius):
        print(f'API 1 drawing a circle at ({x}, {y} with radius {radius})')


class DrawingAPITwo:
    """Implementation-specific abstraction: concrete class two"""

    def draw_circle(self, x, y, radius):
        print(f'API 2 drawing a circle at ({x}, {y} with radius {radius})')


class Circle:
    """Implementation-independent abstraction: for example, there could a rectangle class"""

    def __init__(self, x, y, radius, drawing_api):
        """Initialize the necessary attributes"""
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        """Implementation-specific abstraction taken care of by another class: DrawingAPI"""
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, percent):
        """Implementation-independent"""
        self._radius *= percent

if __name__ == "__main__":
    # Build the first Circle object using API One
    circle1 = Circle(1, 2, 3, DrawingAPIOne())
    # draw a circle
    circle1.draw()

    # Build the second Circle object using API Two
    circle2 = Circle(2, 3, 4, DrawingAPITwo())
    # draw a circle
    circle2.draw()
