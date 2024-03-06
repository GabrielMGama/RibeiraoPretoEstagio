# RibeiraoPretoEstagio
Respostas da Entrevista

## 1) Observe o trecho de código abaixo:

int INDICE = 13, SOMA = 0, K = 0;

enquanto K < INDICE faça _Estrututra de Repetição_

{

K = K + 1;  _K += 1_

SOMA = SOMA + K;  _SOMA += 1_

}

imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA?

[Será Imprimido na tela "91"]
---
## 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:

Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

```python
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
```
---

## 3) Descubra a lógica e complete o próximo elemento:



a) 1, 3, 5, 7, _**9**__

b) 2, 4, 8, 16, 32, 64, __**128**__

c) 0, 1, 4, 9, 16, 25, 36, __**49**__

d) 4, 16, 36, 64, _**100**__

e) 1, 1, 2, 3, 5, 8, __**13**__

f) 2,10, 12, 16, 17, 18, 19, __**200**__

---
## 4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.

Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

[Ligaria um dos interruptores iria na sala verificar qual lâmpada acendeu voltaria, ligaria outro interruptor verificar qual lâmpada acendeu dessa vez, por exclusão o proximo interruptor é a lâmpada que sobrou.]

---
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;

```python
frase = input("Entre com uma frase qualquer: ").strip()

palavras = frase.split()

junto = ''.join(palavras)

inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

print(inverso)
```
---




