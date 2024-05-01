class Gato:
    def __init__(self, nombre: str, edad: int, color: str, raza: str, tamanio: str):
        self.nombre = nombre
        self.edad = edad
        self.color = color
        self.raza = raza
        self.tamanio = tamanio

    def meow(self):
        return f"{self.nombre} dice: ¡Miau!"
    
    def atack(self):
        return f"{self.nombre} ATACO!"

    def defender(self):
        return f"{self.nombre} SE DEFENDIO!"

mi_gato1 = Gato("Lucas", 2, "Blanco y negro", "Garfield", "Peque")

print(f"Nombre del gato: {mi_gato1.nombre}")
print(f"Edad del gato: {mi_gato1.edad} años")
print(f"Color del gato: {mi_gato1.color}")
print(f'Raza del gato: {mi_gato1.raza}')
print(f'Tamaño del gato: {mi_gato1.tamanio}\n\n')

mi_gato2 = Gato("Pedrito", 2, "Negro", "Beng", "Grande")

print(f"Nombre del gato: {mi_gato2.nombre}")
print(f"Edad del gato: {mi_gato2.edad} años")
print(f"Color del gato: {mi_gato2.color}")
print(f'Raza del gato: {mi_gato2.raza}')
print(f'Tamaño del gato: {mi_gato2.tamanio}')

print(mi_gato2.atack())