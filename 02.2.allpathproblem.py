def allpath(n):
    rtnpath = [[1 if (2**a)&b==0 else 0 for a in range(n)]for b in range(2**n)]
    return rtnpath
def rightpath(n):
    getall = allpath(n)
    rtnpath = []
    for path in getall:
        flag = True
        for i in range(len(path)-1):
            if path[i]==0 and path[i+1]==0:
               flag=False
               break
        if flag:
            rtnpath.append(path)
    return rtnpath
n = int(input('계단의 수 : '))
print(len(rightpath(n-1)))