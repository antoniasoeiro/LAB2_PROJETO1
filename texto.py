import random

def cumprimento(texto):
    return f"Olá, {texto}!"
print(cumprimento("Maria Antônia Soeiro"))

def sorteio():
    numeros = [random.randint(1,100) for _ in range(7)]
    media = sum(numeros) / len(numeros)
    return f"Números sorteados: {numeros}, Média: {media:.2f}"

sorteio()