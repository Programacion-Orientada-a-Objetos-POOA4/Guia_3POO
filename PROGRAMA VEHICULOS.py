# Definición de la clase base Vehiculo
class Vehiculo:
    def _init_(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrarInfo(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Año:", self.año)

# Definición de la clase derivada Coche, que hereda de Vehiculo
class Coche(Vehiculo):
    def _init_(self, marca, modelo, año, numeroPuertas):
        # Llamar al constructor de la clase base usando super()
        super().__init__(marca, modelo, año)
        self.numeroPuertas = numeroPuertas

    def mostrarInfo(self):
        # Llamar al método mostrarInfo de la clase base usando super()
        super().mostrarInfo()
        print("Número de Puertas:", self.numeroPuertas)

# Definición de la clase derivada Moto, que hereda de Vehiculo
class Moto(Vehiculo):
    def _init_(self, marca, modelo, año, cilindrada):
        # Llamar al constructor de la clase base usando super()
        super().__init__(marca, modelo, año)
        self.cilindrada = cilindrada

    def mostrarInfo(self):
        # Llamar al método mostrarInfo de la clase base usando super()
        super().mostrarInfo()
        print("Cilindrada:", self.cilindrada, "cc")

# Bloque principal del programa

# Crear instancias de Coche y Moto con nueva información
coche1 = Coche("Ford", "Focus", 2023, 5)  # Cambiar la información del coche 1
moto1 = Moto("Suzuki", "GSX-R750", 2022, 750)  # Cambiar la información de la moto 1

# Llamar al método mostrarInfo() para cada instancia
print("Información del Coche 1:")
coche1.mostrarInfo()

print("\nInformación de la Moto 1:")
moto1.mostrarInfo()
