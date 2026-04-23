def calcular(n1, n2, simbolo):
    if simbolo == "+":
        return n1 + n2
    elif simbolo == "-":
        return n1 - n2
    elif simbolo == "*":
        return n1 * n2
    elif simbolo == "/":
        if n2 != 0:
            return n1 / n2
        else:
            return "Erro: divisão por zero!"
    else:
        return "Operação inválida! Use +, -, * ou /."
    
print(calcular(10, 5, "+"))