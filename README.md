# **Generador de Horarios Automático**

## **Descripción del Proyecto**
Este proyecto genera automáticamente **horarios para asignaturas, profesores y aulas**, respetando restricciones como la disponibilidad de los profesores, la capacidad de las aulas y las preferencias horarias. Se implementa una **interfaz gráfica interactiva** utilizando **Tkinter** para visualizar los horarios generados.

El proyecto utiliza técnicas avanzadas de algoritmos, como **Backtracking** y **optimización heurística**, para encontrar una solución válida y eficiente.

---

## **Características del Proyecto**
- **Evita conflictos**:
  - Un profesor no puede estar asignado a dos clases al mismo tiempo.
  - Un aula no puede ser ocupada por más de una clase en la misma hora.
- **Respeta las restricciones**:
  - Disponibilidad de profesores.
  - Capacidad de las aulas.
  - Horarios preferidos de los profesores.
- **Visualización del horario en una interfaz gráfica**:
  - Cada aula tiene una **pestaña propia**.
  - El horario muestra asignaturas, profesores y aulas organizados por horas y días de la semana.

---

## **Técnicas Algorítmicas Utilizadas**

### **1. Backtracking**
- Es un algoritmo de búsqueda que explora todas las combinaciones posibles para asignar asignaturas a horarios y aulas.
- Si se encuentra un conflicto, el algoritmo **retrocede** (backtrack) y prueba la siguiente combinación.
- **Ventaja**: Garantiza encontrar una solución si existe.

### **2. Optimización con Heurísticas**
Para mejorar la eficiencia del algoritmo y reducir el tiempo de búsqueda, se aplican las siguientes optimizaciones:
- **Ordenamiento de aulas**:
  - Las aulas se ordenan por capacidad para minimizar el desperdicio de espacio:
    ```python
    aulas = sorted(aulas, key=lambda x: abs(x.capacidad - asignatura.tamaño_grupo))
    ```
- **Priorización de horarios preferidos**:
  - Las horas preferidas por los profesores reciben un **peso mayor**, lo que aumenta la probabilidad de ser asignadas primero:
    ```python
    if (dia, hora) in asignatura.profesor.preferencias:
        peso = 0.9  # Alta preferencia
    ```

---

## **Estructura del Algoritmo**

1. **Entrada**:
   - Lista de asignaturas, profesores, aulas y sus restricciones.

2. **Proceso**:
   - Utiliza **Backtracking** para:
     - Verificar si una asignación es válida (`verificar_disponibilidad`).
     - Asignar una clase temporalmente (`asignar_horario`).
     - Retroceder si una asignación genera conflictos (`desasignar_horario`).

3. **Salida**:
   - Un horario válido, respetando todas las restricciones.

---

## **Análisis de Eficiencia**

### **Complejidad Temporal**:
- **Peor caso**: \(O(n \cdot m \cdot k)\), donde:
  - \(n\): Número de asignaturas.
  - \(m\): Número de horas disponibles por día.
  - \(k\): Número de aulas.
- La complejidad puede crecer exponencialmente, pero las **heurísticas** reducen significativamente el espacio de búsqueda al priorizar las combinaciones más prometedoras.

### **Complejidad Espacial**:
- \(O(d \cdot h)\), donde \(d\) es el número de días y \(h\) el número de horas por día.
- La memoria se utiliza para almacenar el horario generado.

### **Optimización**:
- El ordenamiento de aulas y la priorización de horas preferidas hacen que el algoritmo converja más rápido hacia una solución válida.

---

## **Escalabilidad para Grandes Sistemas**
Para implementar este sistema a **gran escala** (universidades con muchas carreras, grupos y profesores), se requieren las siguientes modificaciones:

1. **Base de Datos**:
   - Utilizar una base de datos como **MySQL** o **PostgreSQL** para manejar grandes volúmenes de datos.

2. **Interfaz Web**:
   - Sustituir **Tkinter** por un framework web como **Django** o **Flask** para mejorar la escalabilidad.

3. **Nuevos Algoritmos**:
   - Reemplazar **Backtracking** por técnicas más eficientes:
     - **Programación Lineal Entera (ILP)**: Solución óptima y eficiente.
     - **Algoritmos Genéticos**: Soluciones aproximadas para problemas muy grandes.
     - **CSP (Constraint Satisfaction Problems)**: Adecuado para problemas de asignación con restricciones complejas.

4. **Optimización**:
   - Modelar el problema como un **flujo de red** para aprovechar algoritmos eficientes de flujo máximo.

---

## **Instalación y Ejecución**

### **Requisitos Previos**
- Python 3.x instalado en tu sistema.

### **Ejecución**
1. Descarga el archivo `generador_horarios.py`.
2. Abre una terminal y ejecuta el programa:
   ```bash
   python generar_horarios.py
