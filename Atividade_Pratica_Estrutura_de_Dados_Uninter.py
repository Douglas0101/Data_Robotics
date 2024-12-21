class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.head = None
        self.contador_verde = 201
        self.contador_amarelo = 1

    def inserir_sem_prioridade(self, nodo):
        if not self.head:
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = nodo

    def inserir_com_prioridade(self, nodo):
        if not self.head or self.head.cor == 'V':
            nodo.proximo = self.head
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo and atual.proximo.cor == 'A':
                atual = atual.proximo
            nodo.proximo = atual.proximo
            atual.proximo = nodo

    def inserir(self):
        cor = input("Digite a cor do cartão (A para amarelo ou V para verde): ").upper()
        if cor == 'A':
            numero = self.contador_amarelo
            self.contador_amarelo += 1
        elif cor == 'V':
            numero = self.contador_verde
            self.contador_verde += 1
        else:
            print("Cor inválida! Tente novamente.")
            return

        novo_nodo = Nodo(numero, cor)
        if cor == 'V':
            self.inserir_sem_prioridade(novo_nodo)
        elif cor == 'A':
            self.inserir_com_prioridade(novo_nodo)

    def imprimir_lista_espera(self):
        if not self.head:
            print("A lista de espera está vazia.")
            return

        atual = self.head
        print("Lista de espera:")
        while atual:
            print(f"Cartão {atual.numero} - Cor: {atual.cor}")
            atual = atual.proximo

    def atender_paciente(self):
        if not self.head:
            print("A lista de espera está vazia. Nenhum paciente para atender.")
            return

        paciente = self.head
        self.head = self.head.proximo
        print(f"Chamando paciente com cartão {paciente.numero} para atendimento.")

    def menu(self):
        while True:
            print("\nMenu Principal")
            print("1 - Adicionar paciente à fila")
            print("2 - Mostrar pacientes na fila")
            print("3 - Chamar paciente")
            print("4 - Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.inserir()
            elif opcao == '2':
                self.imprimir_lista_espera()
            elif opcao == '3':
                self.atender_paciente()
            elif opcao == '4':
                print("Encerrando o programa. Até mais!")
                break
            else:
                print("Opção inválida! Tente novamente.")

# Inicializando o programa
if __name__ == "__main__":
    lista = ListaEncadeada()
    lista.menu()
