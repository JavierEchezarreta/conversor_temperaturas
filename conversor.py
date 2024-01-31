def convert2celsius(valor, unidad):
    '''Convierte desde grados °F o °K ---> °C 
    Recibe 2 argumentos: Valor y Unidad 
    y devuelve el valor en °C'''
    if unidad == 'F':
       temperatura_en_celsius = round((valor - 32) * 0.555555556 ,1)
    else:
        temperatura_en_celsius = round(valor - 273.15, 1)
    return temperatura_en_celsius


titulo = 'Conversor de grados Fahrenheit o Kelvin a Celsius'
print(titulo)
print('=' * len(titulo))
while True:
    temperatura = input('Ingrese un valor, ENTER para terminar: ')
    if not temperatura:
        break
    temperatura = float(temperatura)
    unidad_origen = input('Ingrese una letra de unidad: ').upper()
    if unidad_origen == 'F':
        print(temperatura, '°Fahrenheit equivalen a', convert2celsius(temperatura, unidad_origen), '°Celsius')
    elif unidad_origen == 'K':
        print(temperatura, '°Kelvin equivalen a', convert2celsius(temperatura, unidad_origen), '°Celsius')
    else:
        print('Unidad de temperatura incorrecta!')
