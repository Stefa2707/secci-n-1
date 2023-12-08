# 1. Cree un programa que lea la edad de un usuario y muestre cuántos años tendrá el usuario dentro de tantos años como el usuario indique.

edad =  int (input ('ingrese su edad :'))
años =  int (input('ingrese la cantidad de años :'))

suma = edad + años 

print ('tu en esta cantidad de años dentras' , suma)

print ("--------------------------------------------------------------------------------------------------------------------------------------------")


# 2. Cree un programa que lea dos números y muestre su producto, su cociente, su módulo, su suma y su resta

# que operación quiere hacer el husuario 

opcion = input ("para sumar ingrese 1 para restar ingrese 2 para multiplicar ingrese 3 para dividir ingrese 4: " )

# pidamos los numero

numero1 = int (input("ingresa numero 1: "))
numero2 = int (input("ingresa numero 2: "))

# si la opcoón es 1 sumamos 

if opcion == "1": 
    operación = numero1 + numero2
    
    # si la opcoón es 1 sumamos 4

if opcion == "2": 
    operación = numero1 - numero2
    
    # si la opcoón es 1 sumamos 

if opcion == "3": 
    operación = numero1 * numero2
    
    # si la opcoón es 1 sumamos 

if opcion == "4": 
    operación = numero1 / numero2
    
print("resultado de la operación " + str (operación))


print ("--------------------------------------------------------------------------------------------------------------------------------------------")


# Cree un programa que lea el monto de un préstamo y el plazo en meses, y muestre al usuario el valor las cuotas mensuales pagando un interés fijo del 2.7% mensual


nombre =  input ('ingrese su nombre :')
prestamo = float (input('ingrese la cantidad de prestamo :'))
plazo = float (input('ingrese el plazo de meses maximo :'))
intereses = prestamo * 0.27
total1 = prestamo / plazo
total2 = total1 + intereses 

print('------------factura-----------')

print (nombre)
print ('el interes de su prestamo es de :', intereses)
print ('las cuotas mensuales son de :', total2)
