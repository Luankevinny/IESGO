"""
Exercicio fila do banco

"""
# Classe Cliente
class Cliente:
    def __init__(self, nome, prioridade):
        self.nome = nome
        self.prioridade = prioridade

# Função para adicionar um cliente à fila
def adicionar_cliente(fila, nome, prioridade):
    if prioridade:
        fila.insert(0, Cliente(nome, prioridade))
    else:
        fila.append(Cliente(nome, prioridade))

# Função para atender o próximo cliente
def atender_cliente(fila):
    if fila:
        cliente = fila.pop(0)
        print(f"Cliente {cliente.nome} atendido.")
    else:
        print("A fila está vazia.")

# Função para visualizar a fila
def visualizar_fila(fila):
    if fila:
        for cliente in fila:
            print(f"Cliente {cliente.nome}: {cliente.prioridade}")
    else:
        print("A fila está vazia.")

# Função principal
def main():
    # Cria uma lista vazia para armazenar a fila
    fila = []

    # Loop principal
    while True:
        # Exibe o menu de opções
        print("Escolha uma opção:")
        print("1 - Adicionar cliente")
        print("2 - Atender cliente")
        print("3 - Visualizar fila")
        print("4 - Sair")

        # Lê a opção do usuário
        opcao = input("Opção: ")

        # Trata as opções
        if opcao == "1":
            # Solicita o nome do cliente
            nome = input("Nome do cliente: ")

            # Solicita a prioridade do cliente
            prioridade = input("Prioridade do cliente (S/N): ").upper()

            # Adiciona o cliente à fila
            adicionar_cliente(fila, nome, prioridade == "S")
        elif opcao == "2":
            # Atende o próximo cliente
            atender_cliente(fila)
        elif opcao == "3":
            # Visualiza a fila
            visualizar_fila(fila)
        elif opcao == "4":
            # Sai do programa
            break
        else:
            # Imprime um erro
            print("Opção inválida.")

# Chama a função principal
main()
