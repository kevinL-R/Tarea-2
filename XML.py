from xml.dom import minidom
docXML= minidom.parse("ArchivoXML.xml")
usuarios =docXML.getElementsByTagName("usuario")
def imprimir():
    print("----------------------------------------------------------------------------")
    print("-----------------------------Archivo XML------------------------------------")
    print("----------------------------------------------------------------------------")
    for usuario in usuarios:
        sid = usuario.getAttribute("id")
        nombre = usuario.getElementsByTagName("nombre")[0]
        username=usuario.getElementsByTagName("username")[0]
        password = usuario.getElementsByTagName("password")[0]
        estado = usuario.getElementsByTagName("estado")[0]
        print("id: %s" % sid)
        print("nombre:%s" % nombre.firstChild.data)
        print("username:%s" % username.firstChild.data)
        print("password:%s" % password.firstChild.data)
        print("estado:%s" % estado.firstChild.data)
        print()
    print("el tipo de estructura de dato que se obtuvo al cargar el archivo es: ")
    print(type(usuarios))
    print()