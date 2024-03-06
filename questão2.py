num_verifica = int(input("Entre com o número que deseja verificar: "))
achou = False

termo = 0
anterior = 0
proximo = 1

while True:
    print("{} --- ".format(termo), end="")
    
    if num_verifica == termo:
        achou = True
        break
    
    if num_verifica < termo:
        break

    anterior, termo = termo, proximo
    proximo = termo + anterior

    

if achou:
    print(f"\nO número {num_verifica} pertence à sequência.")
else:
    print(f"\nO número {num_verifica} não pertence à sequência.")