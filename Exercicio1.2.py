"""
Exercício 1.2: Gerenciador de Pedidos de Restaurante

Contexto:
Você está ajudando um pequeno restaurante a digitalizar seus processos. Eles querem um programa simples que gerencie os pedidos de seus clientes. Cada pedido pode ter vários itens, e cada item tem um preço associado.

Objetivo:
Crie um programa que permite ao usuário adicionar pedidos, adicionar itens aos pedidos e calcular o total de um pedido.

Requisitos:

O programa deve ter um dicionário de itens_menu onde as chaves são nomes de itens e os valores são os preços. Por exemplo: {"hamburger": 5.50, "batata frita": 2.00, "refrigerante": 1.50}.
Os pedidos podem ser armazenados em um dicionário chamado pedidos, onde as chaves são números de pedido e os valores são outro dicionário contendo os itens pedidos e suas quantidades.
O programa deve permitir que o usuário:
Adicione um novo pedido.
Adicione itens a um pedido existente.
Calcule e exiba o total de um pedido.
Instruções:

Inicialize o dicionário itens_menu com pelo menos 5 itens e seus preços.
Permita que o usuário adicione novos pedidos. Um pedido deve ser outro dicionário com itens e quantidades. Por exemplo: {1: {"hamburger": 2, "refrigerante": 1}} representa um pedido com 2 hambúrgueres e 1 refrigerante.
Permita que o usuário adicione itens a um pedido existente, especificando o número do pedido, o item e a quantidade.
Implemente uma função chamada calcular_total_pedido que aceita um número de pedido e retorna o total desse pedido, multiplicando preços e quantidades e somando todos os itens.
Desafio:

Implemente uma funcionalidade que permite ao usuário remover itens de um pedido ou alterar a quantidade de um item em um pedido.
Permita que o usuário visualize todos os pedidos atuais e seus totais.
Dicas:

Lembre-se de verificar se um item adicionado pelo usuário realmente existe no menu.
Ao calcular o total, lembre-se de multiplicar o preço do item pela quantidade e, em seguida, somar os totais para todos os itens.

"""




menu = {
    "hamburger": 5.50,
    "batata frita": 2.00,
    "refrigerante": 1.50,
    "pizza": 8.00,
    "salada": 3.50
}

orders = {}


def add_order(order_number, items):
    if order_number not in orders:
        orders[order_number] = items
    else:
        orders[order_number].update(items)


def calculate_total(order_number):
    order = orders.get(order_number, {})
    total = sum(menu[item] * quantity for item, quantity in order.items() if item in menu)
    return total


def remove_item(order_number, item):
    if order_number in orders and item in orders[order_number]:
        del orders[order_number][item]


def update_item_quantity(order_number, item, quantity):
    if order_number in orders and item in orders[order_number]:
        orders[order_number][item] = quantity


def display_orders():
    for order_number, items in orders.items():
        total = calculate_total(order_number)
        print(f"Order {order_number}: {items} - Total: ${total:.2f}")


add_order(1, {"hamburger": 2, "refrigerante": 1})
add_order(2, {"pizza": 1, "salada": 1})
display_orders()
