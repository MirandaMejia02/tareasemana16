class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def trabajar(self):
        print(f"{self.nombre} está trabajando")

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    def tomar_decisiones(self):
        print(f"{self.nombre} está tomando decisiones para el departamento {self.departamento}")

class EmpleadoAdministrativo(Empleado):
    def __init__(self, nombre, salario, tarea):
        super().__init__(nombre, salario)
        self.tarea = tarea

    def realizar_tarea(self):
        print(f"{self.nombre} está realizando la tarea de {self.tarea}")

class EmpleadoVentas(Empleado):
    def __init__(self, nombre, salario, zona):
        super().__init__(nombre, salario)
        self.zona = zona

    def vender(self):
        print(f"{self.nombre} está vendiendo productos en la zona {self.zona}")

gerente1 = Gerente("Juan", 5000, "Finanzas")
administrativo1 = EmpleadoAdministrativo("Pedro", 2500, "Facturación")
ventas1 = EmpleadoVentas("María", 3000, "Zona Norte")

empleados = [gerente1, administrativo1, ventas1]

for empleado in empleados:
    empleado.trabajar()

