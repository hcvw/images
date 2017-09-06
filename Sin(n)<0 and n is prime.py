import math
for i in range(2,100):
    is_prime = True
    for j in range(2, int(math.sqrt(i)+1)):
        if i % j == 0:
            is_prime = False
    if is_prime and math.sin(i) < 0:
        print(i)
