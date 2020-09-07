class cordinate:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, another_cordinate):
        x_diff = (self.x - another_cordinate.x)**2
        y_diff = (self.y - another_cordinate.y)**2

        return (x_diff + y_diff)**0.5

def main():
    cordi_1 = cordinate(3, 30)
    cordi_2 = cordinate(4, 8)

    print(cordi_1.distance(cordi_2))


if __name__ == "__main__":
    main()
