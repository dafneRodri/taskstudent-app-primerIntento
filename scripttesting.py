import os

archivos = ["index.html", "tareas.js", "estilos.css"]

print("Iniciando pruebas del proyecto TaskStudentApp")

for archivo in archivos:
    if os.path.exists(archivo):
        print(archivo + " encontrado correctamccccccccccente")
    else:
        print("Error: " + archivo + " no encontrado")

print("Pruebas finalizadas")
