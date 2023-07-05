import random
import csv
import string
import os

def n_random(minimo, maximo):
    return random.randint(minimo, maximo)

def gerar_tamanho_tabelas(minimo, maximo):
    tamanho_tabelas_geradas = []
    n_tabelas = random.randint(minimo, maximo)

    for _ in range(n_tabelas):
        verificacao = True
        while verificacao:
            tamanho = n_random(5, 15)
            if tamanho in tamanho_tabelas_geradas:
                verificacao = True
            else:
                verificacao = False
        tamanho_tabelas_geradas.append(tamanho)

    return tamanho_tabelas_geradas

valores_totais = []

def gerar_valores_binarios(tamanho, n_tabelas_chaves):
    valores_binarios = []

    for i in range(tamanho):
        verificacao = True
        while verificacao:
            valor_binario = ''.join(random.choice('01') for _ in range(n_tabelas_chaves[i]))
            if (valor_binario not in valores_binarios) and (valor_binario not in valores_totais):
                valores_binarios.append(valor_binario)
                verificacao = False
    
    return valores_binarios


def gerar_arquivo_csv(file_name, caracteres, tabelas):
    valores = {}

    for char in caracteres:
        valores[char] = gerar_valores_binarios(len(tabelas), tabelas)

    with open(file_name + '.csv', 'w', newline='') as arquivo:
        escritor_csv = csv.writer(arquivo)
        escritor_csv.writerow(['Caractere'] + [f'Tabela {i+1}' for i in range(len(tabelas))])

        for char in valores:
            escritor_csv.writerow([char] + valores[char])

def gerar_tamanho_tabelas_tabs():
    tamanho = n_random(8, 15)
    return [tamanho] * len(n_tabelas_chaves)

if __name__ == "__main__":
    n_tabelas_chaves = gerar_tamanho_tabelas(3, 10) 
    char_ascii = " " + string.ascii_letters + string.digits + string.punctuation 
    gerar_arquivo_csv('key', char_ascii, n_tabelas_chaves)
    
    print("Qtd tabelas chaves:", len(n_tabelas_chaves))
    print("Tam. tabela chaves:", n_tabelas_chaves)
    
    n_tabelas_tabs = gerar_tamanho_tabelas_tabs()
    char_tabs = list(range(len(n_tabelas_chaves)))
    gerar_arquivo_csv('tabs', char_tabs, n_tabelas_tabs)
    
    print("Tam. tabela tabs:", n_tabelas_tabs)
