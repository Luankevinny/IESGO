"""
Exercício 1.3: Sistema de Gerenciamento de Zoológico

Contexto:
Você foi encarregado de desenvolver um sistema para gerenciar os animais de um zoológico. O zoológico tem vários tipos de animais, e eles precisam de uma forma organizada de acompanhar informações básicas sobre esses animais, como espécie, dieta, idade e habitat.

Requisitos:

Crie uma classe Animal que tenha os seguintes atributos:

nome (nome do animal)
especie (por exemplo, "Leão", "Pinguim", "Cobra")
idade
dieta (por exemplo, "Carnívoro", "Herbívoro", "Onívoro")
A classe Animal também deve ter um método descricao que retorna uma string formatada, descrevendo o animal (por exemplo, "Leo é um Leão de 5 anos que é Carnívoro").

Crie uma classe Zoologico que tenha os seguintes atributos:

animais (uma lista para armazenar instâncias da classe Animal)
A classe Zoologico deve ter os seguintes métodos:

adicionar_animal(self, animal): para adicionar um novo animal ao zoológico.
remover_animal(self, nome): para remover um animal do zoológico usando seu nome.
listar_animais(self): para listar todos os animais no zoológico e suas informações.
Desafio:

Adicione um atributo habitat à classe Animal (por exemplo, "Savana", "Tundra", "Floresta Tropical"). Modifique o método descricao para incluir essa informação.
Na classe Zoologico, adicione um método buscar_por_especie(self, especie) que retorna uma lista de animais dessa espécie específica.
Implemente a possibilidade de listar todos os animais em um habitat específico.
Dicas:

Ao adicionar ou remover animais da lista em Zoologico, lembre-se de usar os métodos da lista, como append ou remove.
Ao listar os animais, use um loop para iterar sobre todos os animais e chamar o método descricao de cada animal.
"""

class Animal:
    def __init__(self, nome, especie, idade, dieta, habitat=None):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.dieta = dieta
        self.habitat = habitat

    def descricao(self):
        if self.habitat:
            return f"{self.nome} é um {self.especie} de {self.idade} anos que é {self.dieta} e vive no habitat {self.habitat}."
        else:
            return f"{self.nome} é um {self.especie} de {self.idade} anos que é {self.dieta}."
class Zoologico:
    def __init__(self):
        self.animais = []

    def adicionar_animal(self, animal):
        self.animais.append(animal)

    def remover_animal(self, nome):
        for animal in self.animais:
            if animal.nome == nome:
                self.animais.remove(animal)
                break

    def listar_animais(self):
        for animal in self.animais:
            print(animal.descricao())

    def buscar_por_especie(self, especie):
        return [animal for animal in self.animais if animal.especie == especie]

    def listar_animais_em_habitat(self, habitat):
        return [animal for animal in self.animais if animal.habitat == habitat]

leao = Animal("Leao", "Leão", 5, "Carnívoro", "Savana")
pinguin = Animal("Pinguin", "Pinguim", 3, "Peixe")


zoo = Zoologico()
zoo.adicionar_animal(leao)
zoo.adicionar_animal(pinguin)

zoo.listar_animais()

lions = zoo.buscar_por_especie("Leão")

savanna_animals = zoo.listar_animais_em_habitat("Savana")

