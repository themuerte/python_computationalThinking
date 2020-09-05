def factorial(number):
    """ n int > 0 
        return n!""" 

    if number == 1:
        return 1
    
    print(number)
    return number * factorial(number - 1)


if __name__ == "__main__":

    number = int(input('ingrese el numero: '))        
    print (f"El factorial de {number} es {factorial(number)}")
