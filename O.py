def maximo(a, b):
    return (a + b + abs(a - b)) // 2
def encontrar_maior(a, b, c):
    max_ab = maximo(a, b)
    max_value = maximo(max_ab, c)
    return max_value
a, b, c = map(int, input().split())
maior = encontrar_maior(a, b, c)
print(maior, "eh o maior")