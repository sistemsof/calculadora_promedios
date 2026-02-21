# calculadora_promedios.py

def ingresar_calificaciones():
    """
    Permite ingresar materias y sus calificaciones.
    Retorna dos listas: nombres y calificaciones.
    """
    materias = []
    calificaciones = []

    while True:
        nombre = input("Ingrese el nombre de la materia: ").strip()
        
        if nombre == "":
            print("El nombre de la materia no puede estar vacío.")
            continue

        # Validación de calificación
        while True:
            try:
                nota = float(input(f"Ingrese la calificación de {nombre} (0 a 10): "))
                
                if 0 <= nota <= 10:
                    break
                else:
                    print("La calificación debe estar entre 0 y 10.")
            
            except ValueError:
                print("Entrada inválida. Debe ingresar un número.")

        materias.append(nombre)
        calificaciones.append(nota)

        continuar = input("¿Desea ingresar otra materia? (s/n): ").strip().lower()
        if continuar != 's':
            break

    return materias, calificaciones


def calcular_promedio(calificaciones):
    """
    Calcula y retorna el promedio de una lista de calificaciones.
    """
    if len(calificaciones) == 0:
        return 0
    return sum(calificaciones) / len(calificaciones)


def determinar_estado(calificaciones, umbral=5.0):
    """
    Determina materias aprobadas y reprobadas según umbral.
    Retorna dos listas con los índices correspondientes.
    """
    aprobadas = []
    reprobadas = []

    for i in range(len(calificaciones)):
        if calificaciones[i] >= umbral:
            aprobadas.append(i)
        else:
            reprobadas.append(i)

    return aprobadas, reprobadas


def encontrar_extremos(calificaciones):
    """
    Encuentra los índices de la calificación más alta y más baja.
    """
    if len(calificaciones) == 0:
        return None, None

    indice_max = calificaciones.index(max(calificaciones))
    indice_min = calificaciones.index(min(calificaciones))

    return indice_max, indice_min


def main():
    print("===== SISTEMA DE CÁLCULO DE PROMEDIOS  =====")

    materias, calificaciones = ingresar_calificaciones()

    if len(materias) == 0:
        print("\n⚠ No se ingresaron materias.")
        print("Programa Finalizado.")
        return

    promedio = calcular_promedio(calificaciones)
    aprobadas, reprobadas = determinar_estado(calificaciones)
    indice_max, indice_min = encontrar_extremos(calificaciones)

    print("\n===== RESUMEN FINAL =====")

    print("\nMaterias Ingresadas:")
    for i in range(len(materias)):
        print(f"- {materias[i]}: {calificaciones[i]}")

    print(f"\nPromedio General: {promedio:.2f}")

    print("\nMaterias Aprobadas:")
    if aprobadas:
        for i in aprobadas:
            print(f"- {materias[i]} ({calificaciones[i]})")
    else:
        print("Ninguna")

    print("\nMaterias Reprobadas:")
    if reprobadas:
        for i in reprobadas:
            print(f"- {materias[i]} ({calificaciones[i]})")
    else:
        print("Ninguna")

    if indice_max is not None:
        print(f"\nMejor calificación: {materias[indice_max]} ({calificaciones[indice_max]})")
        print(f"Peor calificación: {materias[indice_min]} ({calificaciones[indice_min]})")

    print("\nGracias por usar el sistema")


if __name__ == "__main__":
    main()