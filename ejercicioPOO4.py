class Operacion:
    
    def __init__(self):
        self.valor1 = int(input("ingrese un valor"))
        self.valor2 = int(input("ingrese segundo valor"))
        self.sumar()
        self.restar()
        self.multiplicar()
        self.dividir()
    def sumar(self):
        suma = self.valor1+self.valor2
        print("La suma es ",suma)
    def restar(self):
        resta = self.valor1 - self.valor2
        print("La resta es ",resta)
    def multiplicar(self):
        multiplica = self.valor1 * self.valor2
        print("La multiplicación es ",multiplica)
    def dividir(self):
        divide = self.valor1 / self.valor2
        print("La división es ",divide)
        
ejercicio1 = Operacion()


class Alumnos:
    
    def __init__(self):
        self.nombres = []
        self.notas = []
    
    def menu(self):
        opcion = 0
        while opcion !=4:
            print("1 - cargar alumnos")
            print("2 - listar alumnos ")
            print("3 - alumnos destacados")
            print("4 - finalizar programa")
            
            opcion = int(input("ingrese su opción"))
            
            if opcion == 1:
                self.cargar()
            elif opcion == 2:
                self.mostrar()
            elif opcion == 3:
                self.calificaciones()
           
            
        
    
    def cargar(self):
        
        for i in range(5):
            name = input("ingrese su nombre")
            note = float(input("ingrese la nota del alumno"))
            
            self.nombres.append(name)
            self.notas.append(note)
            
    def mostrar(self):
        
        for i in range(5):
            print("Alumno     - - ",self.nombres[i])
            print("Calificación - - ",self.notas[i])
    def calificaciones(self):
        
        for i in range(5):
            if self.notas[i] > 7:
                print("alumnos destacados ")
                print(self.nombres[i],"--",self.notas)
                
alumno1 = Alumnos()
alumno1.menu()

class Agenda:
    
    def __init__(self):
        self.contactos = {}
    
    def menu(self):
        opcion = 0
        
        while opcion != 5:
            print("Menu")
            print("1 - ingresar contactos")
            print("2 - listado de contactos")
            print("3 - consultar contacto")
            print("4 - modificar datos (telefono o correo)")
            print("5 - finalizar programa")
            opcion = int(input("ingrese la opcion que desee"))
            
            if opcion == 1:
                self.carga()
            elif opcion ==2:
                self.mostrar()
            elif opcion ==3:
                self.consulta()
            elif opcion == 4:
                self.modificar()
        
    def carga(self):
        nombre = input("Ingrese nombre del nuevo contacto")
        telefono = input("Ingrese telefono del nuevo contacto")
        mail = input("Ingrese correo del nuevo contacto")
        
        print("----- Contacto creado -----")
        self.contactos[nombre] = [telefono,mail]
        
        
    def mostrar(self):
        
        print("Listado de la agenda ")
        
        for i in self.contactos:
            print(i,self.contactos[i][0],self.contactos[i][1])
            print("-"*8)
    def consulta(self):
        name = input("ingrese el nombre a consultar")
        if name in self.contactos:
            print("Datos contacto consultado: ")
            print(self.contactos[name][0]," - ",self.contactos[name][1])
        else:
            print("El nombre del dato consultado no se encuentra en la agenda")
        
    def modificar(self):
        name = input("nombre del usuario a modificar")
        
        if name in self.contactos:
            eleccion = str(input("¿desea modificar el telefono del contacto? [s/n]"))
                    
            if eleccion == "s":
                self.contactos[name][0] = input("ingrese telefono nuevo")
                print("el telefono se guardo correctamente")
                            
            eleccion = str(input("desea modificar el correo del contacto? [s/n]"))
                  
            if eleccion == "s":
                self.contactos[name][1] = input("se guardo correctamente") 
            
        
        
contacto1 = Agenda()
contacto1.menu()

# Conclusión, dentro de una misma clase, se pueden llamar los metodos self.sumar()
# Generando así menus, o simplificando la forma en la que atraemos la información a otro metodo
# Esta herramienta es muy util. Recordar que seguimos trabajando con la misma clase.

tupla = ()
lista = []
diccionario = {}

def suma(a,b):
    suma = a + b
    print(suma)
class Operaciones:

    def inicializar(self,a,b):

        self.a = a
        self.b = b
    def sumar(self):

        suma = self.a + self.b
        print(suma)
########################
suma1 = Operaciones()
