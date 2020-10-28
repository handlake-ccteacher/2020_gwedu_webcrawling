import random
from pointclass import piPoint

class myPoint(piPoint):
    def __init__(self, x=0.0, y=0.0):
        super().__init__(x, y)

    def setRandom(self):
        self.x = random.random()*100
        self.y = random.random()*100

    def distToOrigin(self):
        origin = myPoint()
        return piPoint.dist(origin, self)

p = myPoint()
n = int(input('몇번 : '))
pin = 0
for i in range(n):
    p.setRandom()
    if p.distToOrigin() < 100 :
        pin += 1
print(f'{pin} point of {n} point ')
print(4*pin/n)