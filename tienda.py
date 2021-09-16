from producto import Comida, Ropa, Electronicos, Entretenimiento

def buscarproducto(lista,id):
    for producto in lista:
        if producto.upc==id:
            return producto
    return None 

def crearproducto(datos):
    if (datos[1] == 'Comida'):
        return Comida(int(datos[3]),datos[0],datos[2],datos[4],int(datos[5]))
    elif (datos[1] == 'Ropa'):
        return Ropa(int(datos[3]),datos[0],datos[2],datos[4],int(datos[5]))
    elif (datos[1] == 'Electronicos'):
        return Electronicos(int(datos[3]),datos[0],datos[2],datos[4],int(datos[5]))
    elif (datos[1] == 'Entretenimiento'):
        return Entretenimiento(int(datos[3]),datos[0],datos[2],datos[4],int(datos[5]))

def esnumero(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

listaproductos=[]
inventario = open("inventario.csv")
for linea in inventario:
    datos = linea.split(",")
    listaproductos.append(crearproducto(datos))
inventario.close()

x="0"
while not x == "6":
    print('Bienvenido a la tienda, ingrese el numero de opcion que guste\n\t1) ver inventario  \n\t2) comprar producto  \n\t3) reabastecer producto \n\t4) registrar producto nuevo\n\t5) guardar estado de tienda\n\t6) Salir del programa')
    x = input()
    if x=="1":
        print("Nombre\tPrecio\tCantidad\tID")
        for producto in listaproductos:
            print(producto.nombre+"\t"+ str(producto.precio)+"\t"+ str(producto.cantidad)+"\t"+ producto.upc)

    elif x=="2":
        print("Inserte el ID del producto que quiere comprar")
        id=input()
        producto=buscarproducto(listaproductos,id)
        if producto:
            print("¿Cuantos productos deseas comprar?")
            cantidad=int(input())
            producto.vender(cantidad)
            print("El producto se ha comprado con exito")
        else :
            print("El producto no se ha encontrado, intente denuevo")
    elif x=="3":
        print("Inserte el ID del producto que quiere reabastecer")
        id=input()
        producto=buscarproducto(listaproductos,id)
        if producto:
            print("¿Cuantos productos deseas reabastecer?")
            cantidad=int(input())
            producto.comprar(cantidad)
            print("El producto "+producto.nombre+" ahora tiene una cantidad de "+str(producto.cantidad))
        else :
            print("El producto no se ha encontrado, intente denuevo")
    elif x=="4":
        print("Inserte la informacion del nuevo producto en el siguiente formato:\n\t\"Id de producto\",\"Tipo de producto\",\"Nombre\",\"Precio\",\"Dato especifico\",\"Cantidad\"")
        datos=input()
        detos = datos.split(",")
        if len(detos)==6 and esnumero(detos[3]) and esnumero(detos[5]):
            listaproductos.append(crearproducto(detos))
        else:
            print("No se recibio los parametros correctos")
        print(len(listaproductos))

    elif x=="5":
        texto=""
        for producto in listaproductos:
            if producto.__class__.__name__=="Comida":
                variableespecial=producto.fechacad
            elif producto.__class__.__name__=="Ropa":
                variableespecial=producto.talla
            elif producto.__class__.__name__=="Electronicos":
                variableespecial=producto.modelo
            elif producto.__class__.__name__=="Entretenimiento":
                variableespecial=producto.anoprod
            texto+=producto.upc+","+producto.__class__.__name__+","+producto.nombre+","+str(producto.precio)+","+variableespecial+","+ str(producto.cantidad)+"\n"
        f = open("inventario.csv", "w")
        f.write(texto)
        f.close()
print("Saliendo del programa")