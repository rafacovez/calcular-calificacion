# Declara variables
pp = 0
sp = 0
propar = 0
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
  pp = int(input("Digite la calificación de su primer parcial: "))
  while pp < 0 or pp > 100:
    pp = int(input("La calificación debe ser un número entre 0 y 100. Por favor, digite la calificación del primer parcial nuevamente: "))
  sp = int(input("Digite la calificación de su segundo parcial: "))
  while sp < 0 or sp > 100:
    sp = int(input("La calificación debe ser un número entre 0 y 100. Por favor, digite la calificación del segundo parcial nuevamente: "))
  ef = int(input("Digite la calificación de su examen final: "))
  while ef < 0 or ef > 100:
    ef = int(input("La calificación debe ser un número entre 0 y 100. Por favor, digite la calificación del examen final nuevamente: "))
  tp = int(input("Digite la calificación de su total práctica: "))
  while tp < 0 or tp > 100:
    tp = int(input("La calificación debe ser un número entre 0 y 100. Por favor, digite la calificación del total práctica nuevamente: "))

# Calcula calificación final
def calcularCalificacion():
  global propar
  global cf
  propar = (pp + sp) / 2
  cf = round(((propar) + ef + tp) / 3)

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