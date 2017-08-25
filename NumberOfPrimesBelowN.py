import math
for n in range(0,100000):
      prime = 1
      if n > 1:
            for i in range(2,n):
                  if(n % i) == 0:
                        break
                  else:
                        prime += 1
p = prime
for p in range(1, 100000):
      a = math.floor( p * math.log(n))
      print(int(a))
