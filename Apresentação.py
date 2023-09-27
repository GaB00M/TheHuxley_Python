ig=int(input("Trabalho aborda Interface Grafica? (0 - Nao 1 - Sim)\n"))
ia=int(input("Trabalho aborda Inteligencia Artificial? (0 - Nao 1 - Sim)\n"))
e=int(input("Trabalho aborda Encapsulamento? (0 - Nao 1 - Sim)\n"))
i=int(input("Trabalho aborda Indentacao? (0 - Nao 1 - Sim)\n"))
s=int(input("Trabalho aborda Structs? (0 - Nao 1 - Sim)\n"))
if (ig==1) or (ia==1):
  if (e==1) and (i==1):
    if(s==1):
      print("Seu trabalho sera avaliado.")
    else:
      print("Seu trabalho nao sera avaliado, nota 0.")
  else:
    print("Seu trabalho nao sera avaliado, nota 0.")
else:
  print("Seu trabalho nao sera avaliado, nota 0.")