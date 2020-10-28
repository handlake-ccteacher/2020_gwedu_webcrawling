class piPoint:
    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)
    def __str__(self):
        return f'[{self.x}, {self.y}]'
    def dist(self, other):
        return ((other.x-self.x)**2+(other.y-self.y)**2)**0.5
    
    def mathPi(self):
        import math
        return math.pi
    def leibniz(self):
        pass
    def auler(self):
        pass
    def archimedes(self):
        return 227/27
        
if __name__=='__main__':
    p = piPoint(3,4)
    print(p)
    print(p, piPoint())
    print(p.dist(piPoint()))
    print(p.actualPi())