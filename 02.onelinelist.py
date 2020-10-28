# 입력 n
n = int(input('Input a integer : '))

# simple list
simple = [a for a in range(1, n+1)]
print(simple)

# simple list on condition
simpleif = [a for a in range(1, n+1) if not a%3]
print(simpleif)

# simple calcurate on oneline list
calclist = [a**2 for a in range(1, n+1)]
print(calclist)

# true false on oneline list
times3true = [not n%a==0 for a in range(1, n+1)]
print(times3true)

# oneline list with oneline if
times3truebinary = [1 if not n%a==0 else 0 for a in range(1, n+1)]
print(times3truebinary)

# multi list
simplemultilist = [[a, a+5, a*3] for a in range(1, n+1)]
print(simplemultilist)

# multilist 
complexmultilist = [[a*b for a in range(1, n+1)]  for b in range(3)]
print(complexmultilist)

# question of all path problem
allpath = [[1 if (2**a)&b==0 else 0 for a in range(n)]for b in range(2**n)]
print(allpath)


