class Point:
    def __init__(self,x , y):
        self.x = x
        self.y = y

    def set(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'X: {self.x} \t Y: {self.y}'

