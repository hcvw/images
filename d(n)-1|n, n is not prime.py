import math
for i in range(3,1000):
    not_prime = False
    for j in range(2, int(math.sqrt(i)+1)):
        if i % j == 0:
            not_prime = True
    if not_prime:
        oldSum = 0
        for n in range(1, ((i/2) + 1)):
            if (i % n) == 0:
                newSum = oldSum + 1
                oldSum = newSum
        if (i % (newSum)) == 0:
            print(i)
