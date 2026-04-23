ano = int(input ("digite o ano: "))
if ano % 400 == 0:
    print (f"{ano} e um ano bissexto")
elif ano % 4 == 0 and ano % 100 != 0:
    print (f"{ano} e um ano bissexto")
else:
    print (f"{ano} nao e um ano bissexto")
