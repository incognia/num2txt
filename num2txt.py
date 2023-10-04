# Definir listas de palabras para los números del 0 al 19 y las decenas
unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve"]
decenas = ["", "", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]

# Función para convertir un número en texto
def numero_a_texto(numero):
    if numero < 0 or numero > 99:
        return "Número fuera de rango"

    if numero < 20:
        return unidades[numero]
    else:
        decena = numero // 10
        unidad = numero % 10
        if unidad == 0:
            return decenas[decena]
        else:
            return decenas[decena] + " y " + unidades[unidad]

# Pedir al usuario que ingrese un número
try:
    numero = int(input("Ingrese un número entre 0 y 99: "))
    resultado = numero_a_texto(numero)
    print(f"El número {numero} en texto es: {resultado}")
except ValueError:
    print("Entrada no válida. Por favor, ingrese un número válido.")
