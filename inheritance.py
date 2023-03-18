class Shape:
    def __init__(self):
        self.color=(0,0,0)
class Rectangle(Shape):
    def __init__(self,w,h):
        Shape.__init__(self)
        self.width=w
        self.height=h
    def Area(self):
        return self.height*self.width
r1=Rectangle(2,3)
print('the width is ',r1.width)
print('the height is ',r1.height)
print('the area is ', r1.Area())
print('color is ',r1.color)



