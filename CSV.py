import csv
def imprimir():
    print("-----------------------------------------------------------------------------")
    print("-----------------------------Archivo CSV-------------------------------------")
    print("-----------------------------------------------------------------------------")
    with open('ArchivoCSV.csv') as File:
        reader = csv.reader(File, delimiter=";")

        for row in reader:
            print(row)
        print("el tipo de estructura de dato que se obtuvo al cargar el archivo es:")
        print(type(row))