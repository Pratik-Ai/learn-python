# first letter of class should be Capital
class Point:
    def __init__(self , x, y):
        self.x = x
        self.y = y

    def move(self, x):
        print(f"move to {x}")
    def draw(self):
        print("draw")

point = Point(10,20)
print(point.x)
point.move(10)
point.draw()