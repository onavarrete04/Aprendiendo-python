class PilaVacia(Exception):
    pass

class Apilar:
    
    def __init__(self):
        
        self.cabesa = BasePila()

    def top(self):
        return self.cabesa

    def push(self, value):
        self.cabesa = self.cabesa.push(value)
    
    def pop(self):
        vieja_cabesa = self.cabesa
        self.cabesa = self.cabesa.pop()
        return vieja_cabesa
    
    def len(self):
        return self.cabesa.len()

    def is_empty(self):
        return self.cabesa.is_empty()

class BasePila:

    def push(self, value):
        return ItemPila(parent=self, value=value)

    def pop(self):
        raise PilaVacia("La pila se encuentra vacia")

    def len(self):
        return 0
    def is_empty(self):
        return True
    def __repr__(self):
        return "Base de la pila"

class ItemPila:

    def __init__(self,parent,value):
        self.parent = parent
        self.value = value

    def push(self,value):
        return ItemPila(parent=self,value=value)

    def pop(self):
        return self.parent

    def len(self):
        return self.parent.len() + 1
    def is_empty(self):
        return False
    def __repr__(self):
        return str(self.value)

Apilando = Apilar()

Apilando.push(1)
print(Apilando.top())

Apilando.push(2)
print(Apilando.top())