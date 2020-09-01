objective = int(input("ingrese un entero: "))
epsilon = 0.01
cont = epsilon**2
answer = 0.0

while abs(answer**2 - objective) >= epsilon and answer <= objective:
    print(abs(answer**2 - objective), answer)
    answer += cont

if abs(answer**2 - objective) >= epsilon:
    print(f"No se esncontro la raiz {objective}")
else:
    print(f"La raiz de {objective} es de {answer}")


