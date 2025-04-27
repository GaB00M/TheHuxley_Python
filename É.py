import math

def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

while True:
    n = int(input())
    if n == -1:
        break
    if eh_primo(n):
        print(1)
    else:
        print(0)
       