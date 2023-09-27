par = []
impar = []
for _ in range(15):
    num = int(input())
    if num % 2 == 0:
        if len(par) < 5:
            par.append(num)
        else:
            for i in range(5):
                print(f"par[{i}] = {par[i]}")
            par = [num]
    else:
        if len(impar) < 5:
            impar.append(num)
        else:
            for i in range(5):
                print(f"impar[{i}] = {impar[i]}")
            impar = [num]
for i in range(len(impar)):
    print(f"impar[{i}] = {impar[i]}")

for i in range(len(par)):
    print(f"par[{i}] = {par[i]}")