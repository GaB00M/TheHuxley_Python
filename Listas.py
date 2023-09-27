notas = []
soma = 0
indice = 1
qunt_notas = (int(input()))
if qunt_notas >0 and qunt_notas <=5:
    for x in range (qunt_notas):
        nota = float(input())
        soma += nota
        notas.append(nota)
    media = (soma/qunt_notas)
    for x in range (qunt_notas):
        print (f"Nota {x+1}: {notas[x]}")
    print (f"Media: {media:.2f}")
else:
    print ("Numero de notas invalido.")