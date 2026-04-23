class NF:
    def __init__(self, numero, tipo, serie, cnpj, razao_social, data, icms, frete, ipi, valor_produto):
        self.numero = numero
        self.tipo = tipo
        self.serie = serie
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.data = data
        self.icms = icms
        self.frete = frete
        self.ipi = ipi
        self.valor_produto = valor_produto
        self.valor_total = 0

    def obter_numero(self):
        print(f"Número da Nota Fiscal: {self.numero}")
        return self.numero

    def obter_data_emissao(self):
        print(f"Data de emissão: {self.data}")
        return self.data

    def alterar_razao_social(self, nova_razao):
        self.razao_social = nova_razao
        print(f"Razão social alterada para: {self.razao_social}")

    def calcular_valor_total(self):
        """Calcula o valor total da NF: valor do produto + frete + ICMS + IPI"""
        self.valor_total = self.valor_produto + self.frete + self.icms + self.ipi
        print(f"Valor total da Nota Fiscal: R$ {self.valor_total:.2f}")
        return self.valor_total


nf1 = NF(
    numero=12345,
    tipo="Saída",
    serie=1,
    cnpj="12.345.678/0001-99",
    razao_social="Empresa XYZ",
    data="23/09/2025",
    icms=50.0,
    frete=30.0,
    ipi=20.0,
    valor_produto=500.0
)

nf1.obter_numero()
nf1.obter_data_emissao()
nf1.alterar_razao_social("Empresa ABC")
nf1.calcular_valor_total()