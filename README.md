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
- Es un algoritmo de búsqueda que explora todas las combinaciones posibles para asignar asignaturas a horarios y aulas. De manera que se han creado funciónes para:
     - Verificar si una asignación es válida.
     - Asignar una clase temporalmente.
     - Retroceder si una asignación genera conflictos.
- **Ventaja**: Garantiza encontrar una solución si existe.

### **2. Optimización con Heurísticas**
Para mejorar la eficiencia del algoritmo y reducir el tiempo de búsqueda, se aplican las siguientes optimizaciones:
- **Ordenamiento de aulas**:
  - Las aulas se ordenan por capacidad para minimizar el desperdicio de espacio:
- **Priorización de horarios preferidos**:
  - Las horas preferidas por los profesores reciben un **peso mayor**, lo que aumenta la probabilidad de ser asignadas primero

---

## **Análisis de Eficiencia**

### **Complejidad Temporal**:
- **Caso intermedio**: \(O(n·m·k)\), donde:
  - \(n\): Número de asignaturas.
  - \(m\): Número de horas disponibles por día.
  - \(k\): Número de aulas.
- La complejidad puede crecer exponencialmente al peor caso O(n!), por lo que se han implementado **heurísticas** que reducir significativamente el espacio de búsqueda al priorizar las combinaciones más prometedoras.

### **Complejidad Espacial**:
- \(O(d·h)\), donde:
  - \(d\): Número de días.
  - \(h\): Número de horas por día.
- La memoria se utiliza para almacenar el horario generado.

### **Optimización**:
- El ordenamiento de aulas y la priorización de horas preferidas hacen que el algoritmo converja más rápido hacia una solución válida.

---

## **Escalabilidad para Grandes Sistemas**
Para implementar este sistema a **gran escala** (universidades con muchas carreras, grupos y profesores), se proponen las siguientes modificaciones:

1. **Base de Datos**:
   - Utilizar una base de datos para manejar grandes volúmenes de datos.

2. **Interfaz Web**:
   - Sustituir **Tkinter** por un framework web como **Django** o **Flask** para mejorar la escalabilidad.

3. **Nuevos Algoritmos**:
   - Reemplazar **Backtracking** por técnicas más eficientes:
     - **Programación Lineal Entera (ILP)**: Solución óptima y eficiente.
     - **Algoritmos Genéticos**: Soluciones aproximadas para problemas muy grandes.

4. **Optimización**:
   - Modelar el problema como un flujo de red. El objetivo de los flujos de red es determinar la cantidad máxima o mínima de recursos que pueden moverse a través de la red cumpliendo ciertas restricciones. 
