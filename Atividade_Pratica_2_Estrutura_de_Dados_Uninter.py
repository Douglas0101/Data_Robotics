class Nodo:
    def __init__(self, sigla, nome_estado):
        self.sigla = sigla
        self.nome_estado = nome_estado
        self.proximo = None

class TabelaHash:
    def __init__(self):
        self.tabela = [None] * 10

    def funcao_hash(self, sigla):
        if sigla == "DF":
            return 7
        else:
            valor_ascii = ord(sigla[0]) + ord(sigla[1])
            return valor_ascii % 10

    def inserir(self, sigla, nome_estado):
        posicao = self.funcao_hash(sigla)
        novo_nodo = Nodo(sigla, nome_estado)

        if not self.tabela[posicao]:
            self.tabela[posicao] = novo_nodo
        else:
            atual = self.tabela[posicao]
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_nodo

    def imprimir_tabela(self):
        for i, head in enumerate(self.tabela):
            print(f"Posição {i}:", end=" ")
            atual = head
            if not atual:
                print("Vazia")
            else:
                while atual:
                    print(f"[{atual.sigla}]", end=" -> ")
                    atual = atual.proximo
                print("None")

# Inicializando os dados dos estados
estados = [
    ("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"), ("AM", "Amazonas"), ("BA", "Bahia"),
    ("CE", "Ceará"), ("DF", "Distrito Federal"), ("ES", "Espírito Santo"), ("GO", "Goiás"),
    ("MA", "Maranhão"), ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"), ("MG", "Minas Gerais"),
    ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"), ("PE", "Pernambuco"), ("PI", "Piauí"),
    ("RJ", "Rio de Janeiro"), ("RN", "Rio Grande do Norte"), ("RS", "Rio Grande do Sul"),
    ("RO", "Rondônia"), ("RR", "Roraima"), ("SC", "Santa Catarina"), ("SP", "São Paulo"),
    ("SE", "Sergipe"), ("TO", "Tocantins")
]

# Criando a tabela hash e inserindo os estados
tabela = TabelaHash()

# Imprimindo a tabela antes de inserções
print("Tabela Hash antes de inserções:")
tabela.imprimir_tabela()

# Inserindo os estados
for sigla, nome_estado in estados:
    tabela.inserir(sigla, nome_estado)

# Imprimindo a tabela após inserir os estados
print("\nTabela Hash após inserir os estados e DF:")
tabela.imprimir_tabela()

# Inserindo estado fictício
estado_ficticio = ("BK", "Bruno Kostiuk")
tabela.inserir(*estado_ficticio)

# Imprimindo a tabela após inserir o estado fictício
print("\nTabela Hash após inserir o estado fictício:")
tabela.imprimir_tabela()
