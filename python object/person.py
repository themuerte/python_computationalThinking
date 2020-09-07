class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self, name_greet):
        return f"hola {name_greet}, me llamo {self.name}"
    
def main():
    name = input("Ingrese su nombre: ")
    age = int(input("Ingrese su edad: "))

    p = person(name, age)
    print(p.greet('bbcita bebe link y bebe whisky'))


if __name__ == "__main__":
    main()

    
