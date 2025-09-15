import datetime
import time

hoy = datetime.datetime.today().weekday()  # 0 = lunes, 6 = domingo
dias_faltan = (3 - hoy) % 7  # 3 es jueves
segundos_faltan = dias_faltan * 24 * 60 * 60

print(f"Esperando {dias_faltan} día(s) hasta el jueves...")
time.sleep(segundos_faltan)
print("Ya es jueves, peda programada ✅")
