import os

libros = []
libros_prestados = []


def registrar_libro():
    try:

        print("Ingrese los datos del libro:" )
        titulo = input("Título: \n")
        autor = input("Autor: \n")
        Año_Publicacion = input("Año de Publicación: \n")
        SKU = input("SKU: \n")

        if titulo == "" or autor == "" or Año_Publicacion == "" or SKU == "":
            print("Error en los datos ingresados. Intente nuevamente.")
    except ValueError:
        print("Error en los datos ingresados. Intente nuevamente.")

    libro = {
         'Título': titulo,
         'Autor': autor,
         'Año de Publicación': Año_Publicacion,
         'SKU': SKU
     }
    
    libros.append(libro)
    print("Libro registrado exitosamente.")


def prestar_libro():
    try:

        nombre_usuario = input("Ingrese su nombre: \n")
        SKU_prestar = input("Ingrese el SKU del libro: \n")
        fecha_prestamo = input("Ingresa la fecha de hoy:\n")

        if SKU_prestar.lower in [libro['SKU'] for libro in libros]:
            libro_prestar = [libro for libro in libros if libro['SKU'] == SKU_prestar][0]
            libros.remove(libro_prestar)
            
        
        elif SKU_prestar not in [libro['SKU'] for libro in libros]:
            print("El SKU ingresado no corresponde a un libro registrado.")
        
        libro_prestado = {
            'Nombre de Usuario': nombre_usuario,
            'SKU': SKU_prestar,
            'Fecha del prestamo': fecha_prestamo,
        }
            

        
        libros_prestados.append(libro_prestado)
        print("Libro prestado exitosamente.")
    except ValueError:
        print("Error en los datos ingresados. Intente nuevamente.")
        



def listar_libros():
    if libros == "":
        print("No hay libros registrados.")
    else:
        for libro in libros:
            print(f"Título: {libro['Título']}\t Autor: {libro['Autor']}\t Año de Publicación: {libro['Año de Publicación']}\t SKU: {libro['SKU']}")


def reporte_prestamos():
    try:
        for libro_prestado in libros_prestados:
            with open('Reporte_prestamos.txt', 'w') as archivo:
                archivo.write(f"Nombre de Usuario: {libro_prestado['Nombre de Usuario']}\t SKU: {libro_prestado['SKU']}\n Fecha de prestamo: {libro_prestado['Fecha del prestamo']}")
                print("El reporte se a generado exitosamente en: ", os.getcwd())
        if libros_prestados == "":
            print("No hay libros prestados.")
    except ValueError:
        print("Error al generar el reporte de los prestamos. ")
           
            
def menu():
    while True:
        try:
            print("\n *** M E N U ***")
            op = int(input("1)Registrar libro\n2)Prestar libro\n3)Listar todos los libros\n4)Imprimir reportes de prestamos\n5)Salir del programa \n "))
            if op == 1: 
                registrar_libro()
            elif op == 2:
                prestar_libro()
            elif op == 3:
                listar_libros()
            elif op == 4:
                reporte_prestamos()
            elif op == 5:
                print("Sliendo del programa...")
                print("Desarrollado por Melquisedec Moreno\n RUN: 21.449.116-9")
                break
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            print("Error en el dato ingresado. Intente nuevamente. ")    
           



        



