while True:  # ciclo while para volver a pedir datos tras excepciones

    try:
        edad = int(input("Ingrese su edad: "))  # edad int

        if edad < 0:  # advertencia edad negativa
            print("ERROR: Edad no puede ser número negativo. Intente nuevamente.") 
        elif edad > 120:   # alerta edad demasiado alta
            print("ERROR: Edad fuera de rango válido.")
        else:  #  rango válido
            print(f"Procesando dato. . . \nEdad correctamente validada: {edad} años.")
            break  #  salir del bucle en caso de estar en rango
        
    except ValueError:  # error en tipo de valor ingresado
        print("E R R O R :  Debes ingresar un número entero. Intente nuevamente. \n")
    except TypeError:
        print("Ha ocurrido un error al ingresar dato. Verifique lo ingresado")
