#Te permiten agrupar datos que pertenecen a una misma entidad
#se agrupan en corchetas {}
diccionario={"name":"ryan",
"lastname":"ray",
"nickname":"faz"}
print(diccionario)

print(type({"name":"ryan",
"lastname":"ray",
"nickname":"faz"}))

producto_biblioteca = {
    "nombre":"book",
    "cantidad": 3,
    "precio": 5.59
}
persona ={
    "primer_nombre":"oscar",
    "apellido_persona":"baena" 
}

print(type(producto_biblioteca))

print(persona.keys())   # la función keys imprime la llave de los diccionarios
print(persona.items())  # la función items imprime los datos referentes a las llaves

# la función del tambien elimina los diccionarios, o si quieres limpiarlos puedes usar clear()

productos = [
    {"name":"book", "precio":10.99}  # una lista puede contener diccionarios
    
]