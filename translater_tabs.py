import csv, random

def carregar_tabelas_de_traducao(csv_file):
    tabelas_de_traducao = []
    with open(csv_file, mode='r') as file:
        leitor = csv.reader(file)
        cabecalho = next(leitor)  # Ler a primeira linha do arquivo CSV (cabeçalho)
        for indice_coluna in range(1, len(cabecalho)):
            tabela_de_traducao = {}
            file.seek(0)  # Reiniciar a leitura do arquivo para cada tabela
            next(leitor)  # Ignorar a primeira linha novamente
            for linha in leitor:
                if len(linha) > indice_coluna:
                    caractere = linha[0]
                    valor_binario = linha[indice_coluna]
                    tabela_de_traducao[caractere] = valor_binario
            tabelas_de_traducao.append(tabela_de_traducao)
    return tabelas_de_traducao


def obter_tabs(texto, tabelas_de_traducao):
    traducao = ""
    contagem_caracteres = {}
    ultimo_indice_tabela = None  # Para armazenar o índice da última tabela escolhida
    
    for char in texto:
        if char not in contagem_caracteres:
            contagem_caracteres[char] = 1
        else:
            contagem_caracteres[char] += 1
            
        indice_tabela = contagem_caracteres[char] - 1
        
        if indice_tabela >= len(tabelas_de_traducao):
            indice_tabela = indice_tabela % len(tabelas_de_traducao)
        
        # Selecionar um índice de tabela aleatório, excluindo o último
        indices_tabelas_disponiveis = list(range(len(tabelas_de_traducao)))
        if ultimo_indice_tabela is not None:
            indices_tabelas_disponiveis.remove(ultimo_indice_tabela)
        indice_tabela = random.choice(indices_tabelas_disponiveis)
        
        tabela_de_traducao = tabelas_de_traducao[indice_tabela]
        
        if char in tabela_de_traducao:
            valor_binario = tabela_de_traducao[char]
            traducao += valor_binario + " "
        
        ultimo_indice_tabela = indice_tabela  # Atualizar o índice da última tabela escolhida
    
    return traducao.strip()

def carregar_tbas_csv(csv_file):
    with open(csv_file, mode='r') as file:
        leitor = csv.reader(file)
        return list(leitor)

tabelas_de_traducao = carregar_tabelas_de_traducao('tabs.csv')
traducao = obter_tabs('5555', tabelas_de_traducao)
