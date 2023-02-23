class Usuario:

    def __init__(self, name):
        self.name = name
        self.amount = 0

    def deposito(self, amount):
        self.amount += amount

    def retiro(self, amount):
        self.amount -= amount

    def mostrar_balance(self):
        print(f"Usuario: {self.name}, Total en cuenta: {self.amount}")

    def transferir_dinero(self, amount, user):
        self.amount -= amount
        user.amount += amount
        self.mostrar_balance()
        user.mostrar_balance()


# creación instancias de clase Usuario
cristina = Usuario('Cristina')
sofia = Usuario('Sofia')
tomas = Usuario('Tomas')

cristina.deposito(1000000)
cristina.deposito(700000)
cristina.deposito(5000000)
cristina.retiro(3500000)
cristina.mostrar_balance()

sofia.deposito(2500000)
sofia.deposito(2000000)
sofia.retiro(400000)
sofia.retiro(100000)
sofia.mostrar_balance()

tomas.deposito(800000)
tomas.retiro(150000)
tomas.retiro(200000)
tomas.retiro(50000)
tomas.mostrar_balance()

sofia.transferir_dinero(400000, cristina)
