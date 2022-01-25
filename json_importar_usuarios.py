import json
from urllib import request


pagina = request.urlopen("https://jsonplaceholder.typicode.com/users")
datos = pagina.read().decode("utf-8")

usuarios_lista = json.loads(datos)

for item in usuarios_lista:
    print("Usuario:")
    print("-"*10)
    # Elementos en diccionario normal -> {}
    print(item["id"],"\n ", item["name"]," \n ",
          item["username"],"\n ",item["email"]) 
    # Elementos en diccionario que tiene un diccionario -> {a,b,c, {a,b,c}}
    print(item["address"]["street"],"\n ",item["address"]["suite"],"\n ",item["address"]["city"],"\n",
          item["address"]["zipcode"])
    # Elementos en diccionario que tiene dos diccionarios -> {a,b,{a,b,c,{}}}
    print(item["address"]["geo"]["lat"]," \n ",item["address"]["geo"]["lng"])
    # Retorno a diccionario simple -> {}
    print(item["phone"],"\n ",item["website"])
    # Retorno diccionario diccionario doble -> {a,b,c,{a,b}}
    print(item["company"]["name"],"\n ",item["company"]["catchPhrase"],"\n ",
          item["company"]["bs"])
    print("-"*10)





