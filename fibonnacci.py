def fibonnacci(number):
    if number == 0 or number == 1:
        return 1

    return fibonnacci(number -1) + fibonnacci(number - 2)


if __name__ == "__main__":
    number = int(input('Ingrese un numero: '))
    print(f"El total es : {fibonnacci(number)}")


#prueba para ver si funciona la conexion ssh con git hub
