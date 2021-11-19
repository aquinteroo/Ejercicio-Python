""" 3) La inmobiliaria Campolanzi, con gran presencia en el centro-oeste del país, nos solicita un software para poder 
administrar las propiedades que posee para su gestión. 
Actualmente la inmobiliaria cuenta con un portfolio importante, donde se destacan estos 5 avisos. 

Localidad: Mina Clavero; Provincia: Córdoba; M2: 1027; Ambientes: 6, Comodidades: Pileta, Parrilla, Quincho; Valor: 
u$s 250000; Código de Aviso: FC327 
Localidad: Villa Giardino; Provincia: Córdoba; M2: 936; Ambientes: 5; Comodidades: Quincho, Cancha de futbol; Valor: 
u$s 300000; Código de Aviso: CD123 
Localidad: Merlo; Provincia: San Luis; M2: 547; Ambientes: 4; Comodidades: Pileta, Playroom; Valor: u$s 178000; 
Código de Aviso: DP143 
Localidad: Alto Pelado; Provincia: San Luis; M2: 765; Ambientes: 7; Comodidades: Cancha de Padel, Pileta, Parrilla; 
Valor: u$s 340000; Código de Aviso: LD987 
Localidad: San Rafael; Provincia: Mendoza; M2: 888; Ambientes: 7; Comodidades: Kayak, Asador, Muelle; Valor: u$s 
410000; Código de Aviso: BL332 

Se solicita hacer un programa que contenga un menú que permita: 
        a. El ingreso de nuevas propiedades con sus respectivas características. 
        b. Poder buscar propiedades que contengan un determinado tipo de comodidad. Las mismas deberán ser 
        mostradas ordenadas por provincia de manera alfabética y valor de forma descendente. 
        c. Top 3 de las provincias con mayor valor promedio por ambiente. Se deberá imprimir: Provincia, valor 
        promedio por ambiente, cantidad de propiedades en portfolio. 
        d. La impresión de un reporte de todas las comodidades disponibles, ordenadas por cantidad de apariciones 
        de manera descendente. Se deberá mostrar: Comodidad, cantidad de apariciones, detalle de avisos en los 
        cuales se encuentra (mostrar el código). 
        e. Mostrar las localidades donde el % de propiedades publicadas con mas de 5 ambientes sea mayor al 50%. 
        Para dichas localidades determinar el valor promedio de las propiedades. Se debe mostrar: Localidad – 
        Porcentaje – Valor promedio.  
Es obligatorio utilizar como mínimo una lista y un diccionario. """

#Armo el diccionario así para no tener problemas con las keys
propiedades = {
                'FC327':['Mina Clavero', 'Córdoba', 1027, 6, ['Pileta', 'Parrilla', 'Quincho'], 250000],
                'CD123':['Villa Giardino', 'Córdoba', 936, 5, ['Quincho', 'Cancha de futbol'], 300000], 
                'DP143':['Merlo', 'San Luis', 547, 4, ['Pileta', 'Playroom'], 178000], 
                'LD987':['Alto Pelado', 'San Luis', 765, 7, ['Cancha de Padel', 'Pileta', 'Parrilla'], 340000], 
                'BL332':['San Rafael', 'Mendoza', 888, 7, ['Kayak', 'Asador', 'Muelle'], 410000]}


#Encontre esta forma de ordenar aunque no me queda muy claro >> 'key=lambda x: (x[1][1], x[1][5])'
lista_ordenada = sorted(propiedades.items(), key=lambda x: (x[1][1], x[1][5]))
print('\n\n')
""" for elemento in lista_ordenada:
    print(elemento) """


#Necesitaría ayuda con el punto C del menú 
diccionario_valor_promedio_por_ambiente = {}

for key, value in propiedades.items():
        diccionario_valor_promedio_por_ambiente[value[1]] = value[5] / value[3 ]
#Al hacer esto ↑ pierdo otro valor para la misma provincia y no se como meter los valores en una lista para la misma key(provincia)
print('\n\n')
print(diccionario_valor_promedio_por_ambiente)"# Ejercicio-Python" 
