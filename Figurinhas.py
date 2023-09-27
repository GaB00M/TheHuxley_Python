m = 0
j = 0
figj = []
figm = []
figurinhas = int(input())
for x in range (figurinhas):
    num_serie = int(input())
    if num_serie%2 != 0:
        m += 1
        if num_serie not in figm:
            figm.append(num_serie)
    else:
        j += 1
        if num_serie not in figj:
            figj.append(num_serie)
print (j)
print (m)
if (sum(figj)) > (sum(figm)):
    print (f'{sum(figj)}')
else:
    print (f'{sum(figm)}')