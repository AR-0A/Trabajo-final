
import tkinter as tk
from tkinter import ttk

class Profesor:
    def __init__(self, nombre, disponibilidad, materias, preferencias):
        self.nombre = nombre
        self.disponibilidad = disponibilidad  # Diccionario: {día: [horas]}
        self.materias = materias  # Lista de materias
        self.preferencias = preferencias  # Lista de horas preferidas (día, hora)

class Aula:
    def __init__(self, id, capacidad, disponibilidad):
        self.id = id
        self.capacidad = capacidad
        self.disponibilidad = disponibilidad  # Diccionario: {día: [horas]}

class Asignatura:
    def __init__(self, nombre, profesor, horas_semanales, grupo, tamaño_grupo):
        self.nombre = nombre
        self.profesor = profesor
        self.horas_semanales = horas_semanales
        self.grupo = grupo
        self.tamaño_grupo = tamaño_grupo

# Algoritmo de Backtracking para generar horarios
def generar_horario(asignaturas, aulas):
    horario = {}  # {día: {hora: [(asignatura, aula, profesor)]}}
    if backtracking(asignaturas, aulas, horario):
        return horario
    else:
        return None

def backtracking(asignaturas, aulas, horario):
    if not asignaturas:
        return True

    asignatura = asignaturas[0]
    aulas = sorted(aulas, key=lambda x: abs(x.capacidad - asignatura.tamaño_grupo))  # Ordenar aulas por capacidad

    for dia, horas in asignatura.profesor.disponibilidad.items():
        for hora in horas:
            if (dia, hora) in asignatura.profesor.preferencias:
                peso = 0.9  # Alta preferencia
            else:
                peso = 0.5  # Baja preferencia

            for aula in aulas:
                if verificar_disponibilidad(horario, dia, hora, asignatura, aula):
                    asignar_horario(horario, dia, hora, asignatura, aula, peso)
                    if backtracking(asignaturas[1:], aulas, horario):
                        return True
                    desasignar_horario(horario, dia, hora, asignatura, aula)

    return False

def verificar_disponibilidad(horario, dia, hora, asignatura, aula):
    # Verifica si el profesor, aula y horario están disponibles
    if dia in horario and hora in horario[dia]:
        for asignado in horario[dia][hora]:
            if asignado[1] == aula or asignado[2] == asignatura.profesor:
                return False
    return True

def asignar_horario(horario, dia, hora, asignatura, aula, peso):
    if dia not in horario:
        horario[dia] = {}
    if hora not in horario[dia]:
        horario[dia][hora] = []
    horario[dia][hora].append((asignatura, aula, asignatura.profesor, peso))

def desasignar_horario(horario, dia, hora, asignatura, aula):
    horario[dia][hora] = [entry for entry in horario[dia][hora] if entry[0] != asignatura]

# Visualización del horario
def mostrar_horario_por_aula(horario, aulas):
    ventana = tk.Tk()
    ventana.title("Horario Generado por Aulas")

    notebook = ttk.Notebook(ventana)
    notebook.pack(expand=True, fill=tk.BOTH)

    horas_semana = [8, 9, 10, 11, 12]  # Horas del día
    dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes"]

    for aula in aulas:
        frame = ttk.Frame(notebook)
        notebook.add(frame, text=f"Aula {aula.id}")

        columnas = ["Horas"]
        for dia in dias_semana:
            columnas.extend([dia.capitalize(), f"Profesor/Aula {dia.capitalize()}"])
        
        tree = ttk.Treeview(frame, columns=columnas, show="headings")
        for col in columnas:
            tree.heading(col, text=col)

        for hora in horas_semana:
            fila = [f"{hora}:00"]
            for dia in dias_semana:
                if dia in horario and hora in horario[dia]:
                    clases = [clase for clase in horario[dia][hora] if clase[1] == aula]
                    if clases:
                        asignatura, _, profesor, _ = clases[0]
                        fila.append(asignatura.nombre)
                        fila.append(f"{profesor.nombre}, {aula.id}")
                    else:
                        fila.extend(["", ""])
                else:
                    fila.extend(["", ""])
            tree.insert("", tk.END, values=fila)

        tree.pack(expand=True, fill=tk.BOTH)

    ventana.mainloop()

# Ejemplo de uso
profesor1 = Profesor("Juan", {"lunes": [9, 10, 11], "miércoles": [10, 11]}, ["Matemáticas"], [("lunes", 9), ("miércoles", 10)])
profesor2 = Profesor("Ana", {"martes": [9, 10], "jueves": [11, 12]}, ["Física"], [("martes", 10), ("jueves", 11)])
profesor3 = Profesor("Carlos", {"lunes": [8, 9], "viernes": [10, 11]}, ["Análisis"], [("lunes", 9), ("viernes", 10)])
profesor4 = Profesor("Elena", {"miércoles": [9, 10, 11], "viernes": [9, 10]}, ["Electromagnetismo"], [("viernes", 9)])
profesor5 = Profesor("José Antonio", {"lunes": [9, 10], "jueves": [10, 11]}, ["Física Cuántica"], [("lunes", 9), ("jueves", 10)])
profesor6 = Profesor("Joaquín", {"martes": [8, 9], "miércoles": [10, 11]}, ["Óptica"], [("miércoles", 10)])
profesor7 = Profesor("Fausto", {"lunes": [11, 12], "viernes": [9, 10]}, ["Algoritmos"], [("viernes", 9)])
profesor8 = Profesor("Gonzalo", {"martes": [9, 10], "jueves": [9, 10]}, ["Electrónica"], [("martes", 9)])
profesor9 = Profesor("David", {"lunes": [10, 11], "miércoles": [9, 10]}, ["Física del Estado Sólido"], [("lunes", 10)])
profesor10 = Profesor("José", {"martes": [10, 11], "jueves": [8, 9]}, ["Estadística"], [("martes", 10)])
profesor11 = Profesor("Borja", {"lunes": [8, 9], "viernes": [11, 12]}, ["Mecánica"], [("viernes", 11)])

aula1 = Aula("A1", 30, {"lunes": [9, 10, 11], "martes": [9, 10], "miércoles": [9, 10, 11], "jueves": [9, 10, 11], "viernes": [9, 10, 11]})
aula2 = Aula("A2", 50, {"lunes": [8, 9, 10, 11], "martes": [8, 9, 10, 11], "miércoles": [8, 9, 10, 11], "jueves": [8, 9, 10, 11], "viernes": [8, 9, 10, 11]})
aula3 = Aula("A3", 20, {"lunes": [9, 10, 11], "martes": [9, 10], "miércoles": [9, 10, 11], "jueves": [9, 10, 11], "viernes": [9, 10, 11]})

asignatura1 = Asignatura("Matemáticas", profesor1, 3, "1A", 25)
asignatura2 = Asignatura("Física", profesor2, 2, "1B", 40)
asignatura3 = Asignatura("Análisis", profesor3, 2, "1C", 18)
asignatura4 = Asignatura("Electromagnetismo", profesor4, 3, "2A", 20)
asignatura5 = Asignatura("Física Cuántica", profesor5, 2, "3A", 15)
asignatura6 = Asignatura("Óptica", profesor6, 2, "3B", 22)
asignatura7 = Asignatura("Algoritmos", profesor7, 2, "2B", 30)
asignatura8 = Asignatura("Electrónica", profesor8, 2, "1D", 35)
asignatura9 = Asignatura("Física del Estado Sólido", profesor9, 2, "3C", 28)
asignatura10 = Asignatura("Estadística", profesor10, 2, "2C", 32)
asignatura11 = Asignatura("Mecánica", profesor11, 2, "3D", 25)

horario = generar_horario([asignatura1, asignatura2, asignatura3, asignatura4, asignatura5, asignatura6, asignatura7, asignatura8, asignatura9, asignatura10, asignatura11], [aula1, aula2, aula3])
if horario:
    mostrar_horario_por_aula(horario, [aula1, aula2, aula3])
else:
    print("No se pudo generar un horario válido.")