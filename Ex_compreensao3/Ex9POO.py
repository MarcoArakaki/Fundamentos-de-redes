class Carro:
    def __init__(self, marca, modelo, cor, ano, valor, consumo, nivel=0.0):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.valor = valor
        self.nivel = nivel
        self.consumo = consumo
        self.distancia_total = 0

    def abastecer(self, litros):
        """Incrementa o nível do tanque de combustível."""
        if litros > 0:
            self.nivel += litros
            print(f"Abastecido: {litros} litros. Nível atual: {self.nivel:.2f} litros.")
        else:
            print("Quantidade inválida para abastecimento.")

    def andar(self, distancia_km):
        """Atualiza o nível de combustível de acordo com a distância percorrida."""
        if distancia_km <= 0:
            print("Distância inválida.")
            return

        combustivel_necessario = distancia_km / self.consumo
        if combustivel_necessario <= self.nivel:
            self.nivel -= combustivel_necessario
            self.distancia_total += distancia_km
            print(f"Veículo andou {distancia_km} km. Combustível restante: {self.nivel:.2f} litros.")
        else:
            print("Combustível insuficiente para percorrer esta distância.")

    def verificar_nivel(self):
        """Calcula quantos litros de combustível foram gastos por km."""
        if self.distancia_total == 0:
            print("O carro ainda não percorreu nenhuma distância.")
            return 0
        consumo_medio = (self.distancia_total / (self.consumo * self.distancia_total / self.consumo))
        print(f"Litros restantes no tanque: {self.nivel:.2f} litros.")
        return self.nivel

    def calcular_imposto(self):
        """Calcula IPVA como 3,5% do valor do carro."""
        ipva = self.valor * 0.035
        print(f"IPVA a pagar: R$ {ipva:.2f}")
        return ipva


carro1 = Carro("Toyota", "Corolla", "Prata", 2020, 90000, consumo=12)
carro1.abastecer(50)
carro1.andar(100)
carro1.verificar_nivel()
carro1.calcular_imposto()