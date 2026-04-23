def media(n1, n2, n3, letra):
    if letra.upper() == "A":
        return (n1 + n2 + n3) / 3
    elif letra.upper() == "P":
        return (n1 * 5 + n2 * 3 + n3 * 2) / (5 + 3 + 2)
    else:
        return "Use 'A' para aritmética ou 'P' para ponderada."
print (media(10,5,10,"p"))