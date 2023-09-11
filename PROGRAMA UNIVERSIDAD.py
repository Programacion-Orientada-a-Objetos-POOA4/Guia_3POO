# Definición de la clase abstracta Persona
class Persona:
    def _init_(self, nombre, apellidos, direccion, tipo_id, nro_id):
        self.nombre = nombre
        self.apellidos = apellidos
        self.direccion = direccion
        self.tipo_id = tipo_id
        self.nro_id = nro_id

    def consultar_info_personal(self):
        pass  # Este método es abstracto y se implementará en las clases hijas

# Definición de la clase Estudiante que hereda de Persona
class Estudiante(Persona):
    def _init_(self, nombre, apellidos, direccion, tipo_id, nro_id, codigo):
        super().__init__(nombre, apellidos, direccion, tipo_id, nro_id)
        self.codigo = codigo

    def consultar_info_personal(self):
        # Método para consultar información personal de un estudiante
        return f"Nombre: {self.nombre} {self.apellidos}, Código: {self.codigo}, Tipo de ID: {self.tipo_id}, Número de ID: {self.nro_id}"

# Definición de la clase Docente que hereda de Persona
class Docente(Persona):
    def _init_(self, nombre, apellidos, direccion, tipo_id, nro_id, escalafon):
        super().__init__(nombre, apellidos, direccion, tipo_id, nro_id)
        self.escalafon = escalafon

    def consultar_info_personal(self):
        # Método para consultar información personal de un docente
        return f"Nombre: {self.nombre} {self.apellidos}, Escalafón: {self.escalafon}, Tipo de ID: {self.tipo_id}, Número de ID: {self.nro_id}"

# Definición de la clase Administrativo que hereda de Persona
class Administrativo(Persona):
    def _init_(self, nombre, apellidos, direccion, tipo_id, nro_id, salario):
        super().__init__(nombre, apellidos, direccion, tipo_id, nro_id)
        self.salario = salario

    def consultar_info_personal(self):
        # Método para consultar información personal de un administrativo
        return f"Nombre: {self.nombre} {self.apellidos}, Salario: {self.salario}, Tipo de ID: {self.tipo_id}, Número de ID: {self.nro_id}"

# Función principal (main) para probar las clases

estudiantes = []
docentes = []
administrativos = []

while True:
    print("Bienvenido a la base de datos UMB")
    print("¿Qué deseas hacer?")
    print("1. Agregar un Estudiante")
    print("2. Agregar un Docente")
    print("3. Agregar un Administrativo")
    print("4. Ver la información de algún Estudiante, Docente, o Administrativo")
    print("5. Salir")

    menu = int(input("Selecciona una opción: "))

    if menu == 1:
        print("Agregar un Estudiante")
        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        direccion = input("Dirección: ")
        tipo_id = input("Tipo de ID: ")
        nro_id = int(input("Número de ID: "))
        codigo = int(input("Código del Estudiante: "))
        estudiante = Estudiante(nombre, apellidos, direccion, tipo_id, nro_id, codigo)
        estudiantes.append(estudiante)
        print("Estudiante agregado correctamente.")

    elif menu == 2:
        print("Agregar un Docente")
        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        direccion = input("Dirección: ")
        tipo_id = input("Tipo de ID: ")
        nro_id = int(input("Número de ID: "))
        escalafon = input("Escalafón del docente: ")
        docente = Docente(nombre, apellidos, direccion, tipo_id, nro_id, escalafon)
        docentes.append(docente)
        print("Docente agregado correctamente.")

    elif menu == 3:
        print("Agregar un Administrativo")
        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        direccion = input("Dirección: ")
        tipo_id = input("Tipo de ID: ")
        nro_id = int(input("Número de ID: "))
        salario = int(input("Salario del Administrativo: "))
        administrativo = Administrativo(nombre, apellidos, direccion, tipo_id, nro_id, salario)
        administrativos.append(administrativo)
        print("Administrativo agregado correctamente.")

    elif menu == 4:
        print("Ver la información de un Estudiante, Docente, o Administrativo")
        print("Selecciona el tipo de persona:")
        print("1. Estudiante")
        print("2. Docente")
        print("3. Administrativo")
        tipo_persona = int(input("Selecciona una opción: "))
        if tipo_persona == 1:
            codigo_estudiante = int(input("Ingrese el código del Estudiante: "))
            for estudiante in estudiantes:
                if estudiante.codigo == codigo_estudiante:
                    print(estudiante.consultar_info_personal())
                    break
            else:
                print("Estudiante no encontrado.")
        elif tipo_persona == 2:
            id_docente = int(input("Ingrese el número de ID del Docente: "))
            for docente in docentes:
                if docente.nro_id == id_docente:
                    print(docente.consultar_info_personal())
                    break
            else:
                print("Docente no encontrado.")
        elif tipo_persona == 3:
            id_administrativo = int(input("Ingrese el número de ID del Administrativo: "))
            for administrativo in administrativos:
                if administrativo.nro_id == id_administrativo:
                    print(administrativo.consultar_info_personal())
                    break
            else:
                print("Administrativo no encontrado.")
        else:
            print("Tipo de persona no válido.")

    elif menu == 5:
        break

    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
