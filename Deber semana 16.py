# Crea un nuevo archivo llamado my_notes.txt.
my_notes = open('my_notes.txt', 'w')

# Método write(): escribir una línea a la vez
my_notes.write("Línea 1: Universidad Estatal Amazonica.\n")
my_notes.write("Línea 2: Carrera Tecnologías de la Información.\n")

# Método writelines(): escribir una lista de líneas
lineas = ["Línea 3: Materia.\n", "Línea 4: Fundamentos de programación.\n"]
my_notes.writelines(lineas)

my_notes.close()

# Método 1. read()
# Abre el archivo my_notes.txt.
my_notes = open('my_notes.txt', 'r')
print('******************************************************')
print('Método 1: read()')
print('******************************************************')
print(my_notes.read())
my_notes.close()

# Método 2. readlines()
my_notes = open('my_notes.txt', 'r')
print('******************************************************')
print('Método 2: readlines()')
print('******************************************************')
for linea in my_notes.readlines():
    print(linea.rstrip('\n'))
my_notes.close()