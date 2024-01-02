class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def __repr__(self):
        return f'<{self.__class__.__name__} object at {hex(id(self))}>'
    
    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print(f"Résultat de l'addition : {resultat}")

operation_instance = Operation()
operation_instance = Operation(nombre1=10, nombre2=20)

print(operation_instance)
print(operation_instance.nombre1)
print(operation_instance.nombre2)
operation_instance.addition()