# Define an interface
class Shape:
    def area(self):
        pass

# Define a class that implements the Shape interface
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Define a class that overrides an inherited method
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

# Define a method to read data from a file and initialize objects
def initialize_from_file(python practice):
    shapes = []
    with open(python practice, 'r') as file:
        for line in file:
            shape_type, data = line.strip().split(':')
            data = [float(d) for d in data.split(',')]
            if shape_type == 'Circle':
                shapes.append(Circle(data[0]))
            elif shape_type == 'Square':
                shapes.append(Square(data[0]))
    return shapes

# Define a method that demonstrates the use of a loop
def print_areas(shapes):
    for shape in shapes:
        print(f"Area of {type(shape).__name__}: {shape.area()}")

# Main program
if __name__ == "__main__":
    shapes = initialize_from_file('python practice')
    print_areas(shapes)
