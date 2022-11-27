# Declara variables
pp = 0
sp = 0
ef = 0
tp = 0
cf = 0
literal = ""
estatus = ""

# Obtiene valores para realizar cálculo de calificación final
def obtenerValores():
  global pp
  global sp
  global ef
  global tp
  pp = int(input("Digite la calificación de su primer parcial" + ": "))
  sp = int(input("Digite la calificación de su segundo parcial" + ": "))
  ef = int(input("Digite la calificación de su examen final" + ": "))
  tp = int(input("Digite la calificación de su total práctica" + ": "))

# Calcula calificación final
def calcularCalificacion():
  global cf
  cf = round((((pp + sp) / 2) + ef + tp) / 3)

# Calcula literal obtenido
def calcularLiteral():
  global cf
  global literal
  if cf > 90:
    literal = "A"
  elif cf > 80:
    literal = "B"
  elif cf > 70:
    literal = "C"
  elif cf > 60:
    literal = "D"
  else:
    literal = "F"

# Calcula estatus obtenido
def calcularEstatus():
  global cf
  global estatus
  if cf > 90:
    estatus = "APROBADO"
  elif cf > 80:
    estatus = "APROBADO"
  elif cf > 70:
    estatus = "APROBADO"
  elif cf > 60:
    estatus = "REPROBADO"
  else:
    estatus = "REPROBADO"

# Muestra resultado en la consola
def mostrarResultado():
  print("El estudiante " + estatus + " la materia en " + literal + " porque su calificación fue de", cf)

# Ejecuta todas las funciones anteriores
def main():
  print('------------------------------')
  print('--Calculador de calificación--')
  print('------------final-------------')
  print('------------------------------')
  obtenerValores()
  calcularCalificacion()
  calcularLiteral()
  calcularEstatus()
  mostrarResultado()

main()