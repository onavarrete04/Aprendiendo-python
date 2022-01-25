import json
from urllib import request


pagina = request.urlopen("https://jsonplaceholder.typicode.com/users")
datos = pagina.read().decode("utf-8")

usuarios_lista = json.loads(datos)

for item in usuarios_lista:
    print("Usuario:")
    print("-"*10)
    # Elementos en diccionario normal -> {}
    print("Id: ",item["id"],"\n Nombre", item["name"]," \n Apellido",
          item["username"],"\n Email",item["email"]) 
    # Elementos en diccionario que tiene un diccionario -> {a,b,c, {a,b,c}}
    print("calle: ",item["address"]["street"],"\n Casa",item["address"]["suite"],"\n Ciudad: ",item["address"]["city"],"\n",
          item["address"]["zipcode"])
    # Elementos en diccionario que tiene dos diccionarios -> {a,b,{a,b,c,{}}}
    print("Latitud: ",item["address"]["geo"]["lat"]," \n Longitud: ",item["address"]["geo"]["lng"])
    # Retorno a diccionario simple -> {}
    print("Telefono: ",item["phone"],"\n Sitio Web: ",item["website"])
    # Retorno diccionario diccionario doble -> {a,b,c,{a,b}}
    print("Compañia: ",item["company"]["name"],"\n Frase: ",item["company"]["catchPhrase"],"\n bs: ",
          item["company"]["bs"])
    print("-"*10)





