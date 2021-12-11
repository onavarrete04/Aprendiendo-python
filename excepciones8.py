# KeyError:


# Se produce cuando se llama a una llave de diccionario erroneamente

try:
    productos = {"manzana":39, "peras":32, "lechuga":17}
    print(productos["sandia"])
except KeyError:
    print("El producto seleccionado no existe")