horas = 5
mins = 45
segs = 0

angulo_minutos = (6 * mins) + (segs / 10)
angulo_horas = (30 * horas) + (mins / 2)

print("Ângulo do ponteiro de horas: " + str(angulo_horas))
print("Ângulo do ponteiro de minutos: " + str(angulo_minutos))
print("Angulo total: " + str(angulo_horas - angulo_minutos))