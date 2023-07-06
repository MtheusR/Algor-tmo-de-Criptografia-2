import cripto_translater, tradutor, gen_tables, funcoes
import os
from colorama import Fore


def opcao_escrever():
    
    if not os.path.isfile('key.csv') or not os.path.isfile('tabs.csv'):
        funcoes.limpar_console()
        funcoes.criar_tabela()
        
    else:
        funcoes.limpar_console()
        input_text = input(chr(8594) + " Arquivos já criados foram encontrados. Deseja gerar novas tabelas? (y/n): ")
        resposta = input_text.lower()
        if resposta == "y":
            funcoes.criar_tabela()
        elif resposta == "n":
            print()
    input()
    funcoes.limpar_console()
    input_text = input("\nDigite um texto: ")
    translation = cripto_translater.translate_text(input_text, cripto_translater.load_translation_tables('key.csv'))

    input_text = input("\n" + chr(8594) + " Deseja salvar essa mensagem em um arquivo? (y/n): ")
    resposta = input_text.lower()
    if resposta == "y":
        file_name = input("\n" + chr(8594) + " Digite o nome do arquivo: ")
        arquivo = open(file_name +".txt", "w")
        arquivo.write(translation)
        arquivo.close()
        print("\n" + chr(0x1F4C1) + Fore.GREEN + " Arquivo " + file_name +".txt salvo com sucesso!\n" + Fore.RESET)
    elif resposta == "n":
        print(f"\n" + chr(128275) + " Texto criptografado: {" + translation + "}\n")

def opcao_ler():
    file_name = input("\n" + chr(8594) + " Digite o nome do arquivo: ")
    # Abrir o arquivo em modo de leitura
    arquivo = open(file_name + ".txt", "r")
    # Ler o conteúdo do arquivo e armazenar em uma variável string
    conteudo_lido = arquivo.read()
    # Fechar o arquivo
    arquivo.close()
    text = tradutor.translate_binary_to_text(conteudo_lido)
    print("\n" + chr(128275) + " Texto traduzido: {" + text + "}")


systema = True
while systema == True:
    funcoes.limpar_console()
    opcoes = ["Escrever mensagem", "Traduzir arquivo", "Sair"]
    opcao = funcoes.curses.wrapper(funcoes.menu_principal, opcoes)

    if opcao == 1:
        opcao_escrever()
        input()

    elif opcao == 2:
        opcao_ler()
        input()