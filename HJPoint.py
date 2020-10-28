class HJPoint:
    def __init__(self, x=0, y=0):
        '''
        create one point coordinate [x, y] default origin[0, 0]
        '''
        self.x = x
        self.y = y
        
    def __str__(self):
        return f'[{self.x}, {self.y}]'

    def distToOrigin(self):
        '''
        distance of Point!
        '''
        return ((self.x**2)+(self.y**2))**0.5
    def move(self, x, y):
        self.x = x
        self.y = y
    def moveTo(self, x, y):
        self.x += x
        self.y += y
        
if __name__=='__main__':
    d1 = HJPoint()
    d2 = HJPoint(3,4)
    print(d1)
    print(d2.distToOrigin())

