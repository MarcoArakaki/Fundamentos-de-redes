nota = float(input("digite a nota: "))
cont = 0
soma = 0
while 0 <= nota <= 10:
    cont +=1
    soma = soma + nota
    nota = float(input("digite a nota: "))
media = soma/cont
print (f"a media das notas e igual a {media}")
    


