def divider(n):
    '''
약수리스트
'''
    # return [a for a in range(1, n+1) if not n%a]
    rtn = real_divider(n)
    rtn.append(n)
    return rtn


def real_divider(n):
    '''
진약수 : 자신을 제외한 약수
'''
    return [a for a in range(1, n//2+1) if not n%a]


def is_sosu(n):
    '''
소수판별
'''
    return len(divider(n))==2

def sosu(n):
    '''
소수리스트
'''
    return [a for a in range(2, n+1) if is_sosu(a)]

def last_sosu(n):
    '''
마지막 소수
'''
    for _ in range(n, n//2, -1):
        if is_sosu(_):
            return _
    return 2

def is_friend(a, b):
    '''
우정수 : a의 진부분집합의 합이 b와 같고, b의 진부분집합의 합이 a와 같은 두 수 (220, 284), (1194, 1210), (2620), (2924) 등등...
'''
    return sum(real_divider(a)) == b and a == sum(real_divider(b))

def is_perfect_number(n):
    '''
완전수 : 진부분집합의 합이 자신과 같은수 6, 28, 496, 8128 등등... 
'''
    return n == sum(real_divider(n))


def is_wedding_number(a, b):
    '''
혼약수 : 1을 제외한 진약수의 합과 서로의 수가 같은수(48, 75), (140, 195), (1575, 1848) 등등... 
'''
    return sum(real_divider(a))-1 == b and a == sum(real_divider(b))-1


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    def __str__(self):
        return f'[{self.x}, {self.y}]'
        
if __name__=='__main__':
    for a in range(1, 100):
        if is_perfect_number(a):
            print(a)
    print(real_divider(6))
    print(divider(6))
    print(is_friend(220, 284))
    print(is_wedding_number(48, 75))
