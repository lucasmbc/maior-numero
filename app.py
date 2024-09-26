from functools import reduce

def maior_numero(num1, num2, num3):
    return reduce(max, [num1, num2, num3])

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

maior = maior_numero(n1, n2, n3)
print(f"O maior número é: {maior}")
