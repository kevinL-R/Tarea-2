import json

def readJson():
    file = open('ArchivoJSON.json')
    data = json.load(file)
    file.close()

    return data

def imprimir():
    dict = readJson()
    print("----------------------------------------------------------------------------")
    print("-----------------------------Archivo JSON-----------------------------------")
    print("----------------------------------------------------------------------------")
    for elemento in dict:
        print(elemento)
    print("el tipo de estructura de dato que se obtuvo al cargar el archivo es:")
    print(type(elemento))
    print()