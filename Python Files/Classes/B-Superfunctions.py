class rectangle :
    def __init__(self,width,length):
        self.width=width
        self.length=length

class square (rectangle):
    def __init__(self, width, length):
        super().__init__(width, length)
    def area (self):
        return self.width*self.length

class cube (rectangle):
    def __init__(self, width, length,height):
        super().__init__(width, length)
        self.height=height
    def volume(self):
        return self.width*self.height*self.length

Square=square(3,3)      
Cube  =cube(4,4,4)
print(square.area())
print(cube.volume())