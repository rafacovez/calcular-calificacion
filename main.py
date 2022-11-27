def calcular():
  literal = ""
  estatus = ""
  pp = int(input("Digite la calificación de su primer parcial" + ": "))
  sp = int(input("Digite la calificación de su segundo parcial" + ": "))
  ef = int(input("Digite la calificación de su examen final" + ": "))
  tp = int(input("Digite la calificación de su total práctica" + ": "))
  cf = round((((pp + sp) / 2) + ef + tp) / 3)
  if cf > 90:
    literal = "A"
    estatus = "APROBADO"
  elif cf > 80:
    literal = "B"
    estatus = "APROBADO"
  elif cf > 70:
    literal = "C"
    estatus = "APROBADO"
  elif cf > 60:
    literal = "D"
    estatus = "REPROBADO"
  else:
    literal = "F"
    estatus = "REPROBADO"
  print("El estudiante " + estatus + " la materia en " + literal + " porque su calificación fue de", cf)

def main():
  print('------------------------------')
  print('--Calculador de calificación--')
  print('------------final-------------')
  print('------------------------------')
  calcular()

main()