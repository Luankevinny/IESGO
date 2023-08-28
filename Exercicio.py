def contar_palavras(frase):
    palavras = frase.split()
    return len(palavras)

def contar_vogais(frase):
    frase = frase.lower()
    vogais = 'aeiou'
    count = 0
    for letra in frase:
        if letra in vogais:
            count += 1
    return count

def substituir_python_por_java(frase):
    return frase.replace('Python', 'Java')

def converter_para_minusculas(frase):
    return frase.lower()

def palavras_unicas(frase):
    palavras = frase.lower().split()
    palavras_unicas = set(palavras)
    return list(palavras_unicas)

def ordenar_alfabeticamente(frase):
    palavras = frase.split()
    palavras.sort()
    return ' '.join(palavras)

while True:
    print("Menu de Opções:")
    print("1. Conte o número total de palavras digitadas.")
    print("2. Conte o número de vogais na palavra digitada.")
    print("3. Substitua todas as ocorrências da palavra 'Python' por 'Java'.")
    print("4. Converta todas as letras da string para minúsculas.")
    print("5. Crie uma lista com todas as palavras únicas encontradas na string.")
    print("6. Imprima as palavras na string em ordem alfabética.")
    opcao = input("Digite a opção desejada (ou 's' para sair): ")

    if opcao == '1':
        frase = input("Digite uma frase: ")
        print(f"Total de palavras: {contar_palavras(frase)}")
    elif opcao == '2':
        palavra = input("Digite uma palavra: ")
        print(f"Total de vogais: {contar_vogais(palavra)}")
    elif opcao == '3':
        frase = input("Digite uma frase: ")
        nova_frase = substituir_python_por_java(frase)
        print(f"Frase com substituição: {nova_frase}")
    elif opcao == '4':
        frase = input("Digite uma frase: ")
        nova_frase = converter_para_minusculas(frase)
        print(f"Frase em minúsculas: {nova_frase}")
    elif opcao == '5':
        frase = input("Digite uma frase: ")
        palavras_unicas_lista = palavras_unicas(frase)
        print(f"Palavras únicas: {palavras_unicas_lista}")
    elif opcao == '6':
        frase = input("Digite uma frase: ")
        frase_ordenada = ordenar_alfabeticamente(frase)
        print(f"Palavras em ordem alfabética: {frase_ordenada}")
    elif opcao == 's':
        break
    else:
        print("Opção inválida. Tente novamente.")
