class Point:
    def __init__(self,x , y):
        self.x = x
        self.y = y

    def set(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print (f'X: {self.x}, Y: {self.y}')
