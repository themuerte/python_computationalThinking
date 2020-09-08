
class rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height


class square(rectangle):
    def __init__(self, side):
        super().__init__(side, side)


if __name__ == "__main__":
    rectangle1 = rectangle(3, 4)
    print(f"El area del rectangulo es {rectangle1.area()}")
    
    square1 = square(5)
    print(f"El area del cuadrado es {square1.area()}")
    