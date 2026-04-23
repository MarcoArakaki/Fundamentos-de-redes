def horario(hora, min, sec):
    hora = hora * 3600
    min = min * 60
    res = hora + min + sec
    print(f"tempo convertido para segundos = {res}")
horario(1,1,1)
