"""
Contexto:
Você foi contratado para criar um simples sistema de gerenciamento para uma pequena biblioteca. Os requisitos iniciais são criar um programa que permita ao usuário gerenciar livros e membros da biblioteca.

Requisitos:

A biblioteca deve ser capaz de armazenar informações sobre os livros, como título, autor e status (emprestado ou disponível).
A biblioteca deve também ser capaz de armazenar informações sobre os membros, como nome e os livros que eles emprestaram.
Implemente funcionalidades para adicionar livros, emprestar livros a membros e retornar livros.

Instruções:

Crie uma classe chamada Livro que tenha os seguintes atributos: titulo, autor e status. Por padrão, todos os livros devem ter o status "disponível".

Crie uma classe chamada Membro que tenha os seguintes atributos: nome e livros_emprestados (uma lista).

Crie uma classe chamada Biblioteca que tenha os seguintes atributos: livros (um dicionário com o título do livro como chave e a instância do livro como valor) e membros (um dicionário com o nome do membro como chave e a instância do membro como valor).

Na classe Biblioteca, crie os seguintes métodos:

adicionar_livro(self, livro): Adiciona um livro ao dicionário de livros.
registrar_membro(self, membro): Adiciona um membro ao dicionário de membros.
emprestar_livro(self, titulo_livro, nome_membro): Empresta um livro para um membro se o livro estiver disponível.
retornar_livro(self, titulo_livro, nome_membro): Retorna um livro que estava emprestado.


Desafio:

Adicione funcionalidades para remover livros ou membros.
Implemente uma busca para encontrar um livro ou membro por nome.
Dicas:

Use dicionários para armazenar livros e membros na classe Biblioteca para fácil acesso.
Ao emprestar um livro, atualize o status do livro e a lista de livros emprestados do membro.
Ao retornar um livro, faça o processo inverso do empréstimo.
"""


class Biblioteca:
    def __init__(self):
        self.livros =  {}
        self.membros = {}

    def adicionar_livro(self, livro):
        self.livros[livro.titulo] = livro

    def registrar_membro(self, membro):
        self.membros[membro.nome] = membro

    def emprestar_livro(self, titulo_livro, nome_membro):
        livro = self.livros.get(titulo_livro)
        membro = self.membros.get(nome_membro)
        if livro and membro and livro.status == "disponível":
            livro.status = "emprestado"
            membro.livros_emprestados.append(livro)

    def retornar_livro(self, titulo_livro, nome_membro):
        livro = self.livros.get(titulo_livro)
        membro = self.membros.get(nome_membro)
        if livro and membro and livro.status == "emprestado" and livro in membro.livros_emprestados:
            livro.status = "disponível"
            membro.livros_emprestados.remove(livro)
