# 1) O valor da variável soma vai ser 12

# 2)
def fibo(n):
    i = True
    num = 0
    num1 = 0
    num2 = 1
    lista = []

    while i:
        lista.append(num2)
        if num2 == n:
            i = False
        elif num2 > n:
            i = False
            return "não pertence ao fibonacci"
        num = num1
        num1 = num2
        num2 = num + num1
        
    return "pertence ao fibonacci"
def main():
    num = int(input("digite um numero: "))
    result = fibo(num)
    print(result)
main()


# 3)
# a) 9 apenas impares
# b) 128 o dobro da anterior
# c) 49 somando apenas numeros impares
# d) 100 o dobro do numero vezes 4, sequencia quadratica
# e) 13 sequencia fibbonacci
# f) não sei responder, mas pesquisei e vi que seria 200 por começar em D

# 4) Eu ligaria duas lampadas depois olharia qual nao ligou,
# voltaria e desligaria uma para ver qual desligou e assim saberia qual interruptor controla cada uma

