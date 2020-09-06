objective = int(input('ingresa un entero: '))

answer = 0

while answer**2 < objective:
    ###print(answer)###
    answer += 1

if answer**2 == objective:
    print(f"La raiz cuadrada es: {objective} es {answer}")
else:
    print(f"El {objective} no tiene una raiz cuadrada exacta")