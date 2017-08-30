seconds_str = input("Por favor, entre com o número de segundos que deseja converter: ")

total_seconds = int(seconds_str)

days = total_seconds // (3600 * 24)
hours_rest = total_seconds % (3600 * 24)
hours = hours_rest // 3600
seconds_rest = total_seconds % 3600
minutes = seconds_rest // 60
final_seconds = seconds_rest % 60

print(days,"dias,", hours, "horas,", minutes, "minutos e",final_seconds, "segundos.")
