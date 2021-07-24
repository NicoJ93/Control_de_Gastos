#Gastos

"""App que almacene entrada y salida de dinero y actualice los montos"""

dinero_actual = 0

def ingresos():     #Actualiza el monto que va a disponer el usuario para gastar en un periodo de tiempo
    dinero_ingresado = int(input("Monto del dinero recibido: "))
    dinero_total = dinero_actual + dinero_ingresado
    return dinero_total

def ahorros():        #Actualiza los ahorros del usuario en base a lo que ya tenía y lo que separó en esta nueva instancia
    ahorro = int(input("Monto a ahorrar: "))
    dinero_ahorrado = ahorro + monto_ahorrado
    return dinero_ahorrado

def opciones_operacion():
    gastos = 1      #Son las opciones según quiera proceder el usuario
    entrada_dinero = 2
    para_ahorrar = 3
    eleccion = int(input("Si quiere anotar un gasto presione 1, si quiere agregar dinero presione 2, si quiere guardar en sus ahorros presione 3:"))

def accion_elegida(opciones_operacion):
    opciones_operacion = accion_usuario
    global dinero_en_caja
    if accion_usuario == 1:
        monto_gastado = int(input("Cuánto gastó?"))
        dinero_en_caja = dinero_en_caja - monto_gastado
        print (f"Usted ahora tiene para gastar ${dinero_en_caja}")
        return dinero_en_caja
    elif accion_usuario == 2:
        monto_nuevo = int(input("Cantidad de dinero a añadir para gastos: "))
        dinero_en_caja = dinero_en_caja + monto_nuevo
        print (f"Usted ahora tiene para gastar ${dinero_en_caja}")
        return dinero_en_caja
    elif accion_usuario == 3:
        nuevos_ahorros = int(input("Cuanto dinero mas va a ahorrar?"))
        dinero_en_tarro = dinero_en_tarro + nuevos_ahorros
        print(f"Usted tiene ahorrados ${dinero_en_tarro}")
        return dinero_en_tarro
    else:
        print("Ingrese una opción válida")

accion_elegida()