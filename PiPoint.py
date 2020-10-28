from HJPoint import HJPoint
import random

class PiPoint(HJPoint):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        self.max = 100
    def setRandomPoint(self):
        self.x = random.random()*self.max
        self.y = random.random()*self.max
        
if __name__=='__main__':
    p1 = PiPoint()
    print(p1)
    total = int(input('점몇개 : '))
    inner = 0

    for _ in range(total):
        p1.setRandomPoint()
        if p1.distToOrigin() < p1.max:
            inner += 1
        print(f'{_+1} {inner}, {total} : {4*inner/(_+1):2.5}')

