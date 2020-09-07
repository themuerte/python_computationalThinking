 
class washing_machine:

    def __init__(self):
        pass

    def washing(self, temperature = 'hot'):
        self._fill(temperature)
        self._add_soap()
        self._wash()
        self._centrifuge()
    
    def _fill(self, temperature):
        print('se esta llenando el tamque')

    def _add_soap(self):
        print('se esta anadiendo jabon')

    def _wash(self):
        print('lavando...')

    def _centrifuge(self):
        print('inicia el lavado')


def main():
    washingMachine = washing_machine()
    washingMachine.washing()

if __name__ == "__main__":
    main()





