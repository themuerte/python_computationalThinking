
class person:

    def __init__(self, name):
        self.name =  name 

    def get_moving(self):
        print('caminando...')


class cyclist(person):

    def __init__(self, name):
        super().__init__(name)

    def get_moving(self):
        print('pedaleo...')
    
class engineer(person):
    def __init__(self, name, profession):
        super().__init__(name)
        self.profession = profession

    def get_moving(self):
        print('caminando...... con estilo')
    
    def job(self, name_boss):
        print(f'{self.name} trabajando para {name_boss} como {self.profession}')


def main():
    person1 = person('Eduardo')
    person1.get_moving()

    cyclist1 = cyclist('luis')
    cyclist1.get_moving()

    engineer1 = engineer('Eduardo','ingenierio de sistemas')
    engineer1.get_moving()
    engineer1.job('carlos pellas')


if __name__ == "__main__":
    main()
