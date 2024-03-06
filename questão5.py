frase = input("Entre com uma frase qualquer: ").strip()

palavra = frase.split()

junto = ''.join(palavra)

inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

print(inverso)

