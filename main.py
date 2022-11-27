# Declara variables
pp = "primer parcial"
sp = "segundo parcial"
ef = "examen final"
pt = "práctica total"

# Crea arrays para ahorrar líneas de código
variables = [pp, sp, ef, pt]
calificaciones = []

# Pide al usuario digitar calificaciones obtenidas y las guarda en array calificaciones[]
def digiteCalificaciones():
  i = 1
  for x in variables:
    calificaciones.append(input("Digite la calificación de su " + x + ": "))
    i += 1
    if i > 4:
      break

# Calcula el promedio parcial y la calificación final obtenidos
def calcularCalificacionFinal():
  totalParcial = (int(calificaciones[0]) + int(calificaciones[1])) / 2
  calificacionFinal = (totalParcial + int(calificaciones[2]) + int(calificaciones[3])) / 3
  print("El estudiante pasó la materia en", literal, ", y su calificación final fue de", round(calificacionFinal), ".")

def main():
  print('------------------------------')
  print('--Calculador de calificación--')
  print('------------final-------------')
  print('------------------------------')
  digiteCalificaciones()
  calcularCalificacionFinal()

main()