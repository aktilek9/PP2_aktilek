x = lambda a : a + 10
print(x(5)) 

def myfunc(n):
  return lambda a : a * n 

doubler = myfunc(2)

print(doubler(5))