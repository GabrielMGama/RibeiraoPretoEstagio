frase = input("Entre com uma frase qualquer: ").strip()

palavras = frase.split()

junto = ''.join(palavras)

inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

print(inverso)

