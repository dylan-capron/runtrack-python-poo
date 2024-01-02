class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def __repr__(self):
        return f'<{self.__class__.__name__} object at {hex(id(self))}>'

operation_instance = Operation()
operation_instance = Operation(nombre1=10, nombre2=20)

print(operation_instance)
print("Valeur de nombre1 :", operation_instance.nombre1)
print("Valeur de nombre2 :", operation_instance.nombre2)