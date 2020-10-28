from gwedu import Point
import random

class PIPoint(Point):
    '''
        PI의 근사치를 구하기 위한 클래스
    '''
    def __init__(self, x=0.0, y=0.0, size=100):
        super().__init__(x,y)
        self.size = size
    def setRandom(self):
        '''
            size * size 공간에 무작위로 점을 배치함.
        '''
        self.x = random.random()*self.size
        self.y = random.random()*self.size
    def distToOrigin(self):
        '''
            원점과의 거리를 구함.
        '''
        return ((self.x**2)+(self.y**2))**0.5

if __name__=='__main__':
    tempPoint = PIPoint()
    n = int(input('몇개의 점으로 테스트 할까요 ? '))
    oval = 0
    for i in range(1, n+1):
        tempPoint.setRandom()
        if tempPoint.distToOrigin() < tempPoint.size:
            oval += 1
        print(f'{i}번 : {4*oval/i}')


