import os

# Ruta donde se debería encontrar el archivo deploy.py
ruta_esperada = os.path.expanduser("~/GOMA/heroku/goma-app-clean-new/deploy.py")

# Verificar si el archivo deploy.py existe en la ruta especificada
if os.path.isfile(ruta_esperada):
    print(f"Archivo 'deploy.py' encontrado en: {ruta_esperada}")
else:
    print(f"Error: 'deploy.py' no encontrado en: {ruta_esperada}")

# Verificar el directorio actual
directorio_actual = os.getcwd()
print(f"Directorio actual: {directorio_actual}")

# Comprobar si el directorio actual es el esperado
directorio_esperado = os.path.expanduser("~/GOMA/heroku/goma-app-clean-new")
if directorio_actual == directorio_esperado:
    print("Estás en el directorio correcto.")
else:
    print(f"No estás en el directorio correcto. Navega a: {directorio_esperado}")
