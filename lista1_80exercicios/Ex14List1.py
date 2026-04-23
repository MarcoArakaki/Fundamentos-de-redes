n1 = float(input ("digite a 1 nota: "))
n2 = float(input ("digite a 2 nota: "))
if n1 >= 0 and n1 <= 10 and n2 >= 0 and n2 <= 10:
    res = (n1 + n2)/2
    print (f"a media do aluno e: {res}")
else:
    print ("nota invalida")
    exit