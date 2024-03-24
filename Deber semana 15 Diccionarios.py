# Diccionario

informacion_personal = {
    'Nombre':'Victor',
    'Edad':32,
    'Ciudad':'Portoviejo',
    'Provincia':'Manabí',
}
print('----------------------')
print('Diccionario Original')
print('----------------------')
for clave, valor in informacion_personal.items():
    print(f'{clave} : {valor}')

# Clave "ciudad" y modifícalo con una ciudad diferente.
informacion_personal['Ciudad'] = 'Portoviejo'
informacion_personal['Provincia'] = 'Manabí'

# Nueva clave-valor al diccionario "profesion"
informacion_personal['Profesion'] = 'Estudiante'

# Verifica si la clave "telefono" existe
if 'Telefono' not in informacion_personal:
    informacion_personal['Telefono'] = '0913454123'

# Elimina la clave "edad" del diccionario
# del informacion_personal['edad']
informacion_personal.pop('Edad')

print('----------------------')
print('Diccionario Modificado')
print('----------------------')
for clave, valor in informacion_personal.items():
    print(f'{clave} : {valor}')