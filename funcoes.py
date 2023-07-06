import time, curses, sys, string, os
from colorama import Fore
import gen_tables

def limpar_console():
    if os.name == 'nt':
        _ = os.system('cls')

def print_files_main():
    print()
    print('+-------------------------------------------+');
    print('|             ARQUIVOS CRIADOS              |');
    print('+-------------------------------------------+');
    time.sleep(0.5) 

def print_file(csv_filename):
    print(f"| {csv_filename:<23} | \033[94mSuccessful\033[0m      |")
    print("+-------------------------+-----------------+")
    time.sleep(0.3) 

import string
from rich.console import Console
from rich.table import Table
from rich import box

def criar_tabela():
    limpar_console()
    print(chr(0x1F4DD) + Fore.GREEN +" Tabelas geradas com secesso\n" + Fore.RESET)
    n_tabelas_chaves = gen_tables.gerar_tamanho_tabelas(5, 10)
    char_ascii = " " + string.ascii_letters + string.digits + string.punctuation
    gen_tables.gerar_arquivo_csv('key', char_ascii, n_tabelas_chaves)
    
    num_tabelas_tabs = gen_tables.gerar_tamanho_tabelas_tabs(n_tabelas_chaves)
    char_tabs = list(range(len(num_tabelas_tabs)))
    gen_tables.gerar_arquivo_csv('tabs', char_tabs, num_tabelas_tabs)

    header = ["Arquivo", "Qtd. tabelas", "Tam. tabelas"]

    dados = [
        ["key.csv", str(len(n_tabelas_chaves)), str(n_tabelas_chaves)],
        ["tabs.csv", str(len(n_tabelas_chaves)), str(num_tabelas_tabs)]
    ]

    console = Console()
    table = Table(show_header=True, header_style="bold magenta", box=box.ROUNDED)
    table.add_column(header[0], style="dim", width=15)
    table.add_column(header[1], style="dim", width=15)
    if len(n_tabelas_chaves) > 6:         
        table.add_column(header[2], style="dim", width= (((len(n_tabelas_chaves) - 6) * 5)+25))
    else:
        table.add_column(header[2], style="dim", width=25)

    for row in dados:
        table.add_row(*row)

    console.print(table)        

def exibir_menu(stdscr, opcoes, selecao):
    stdscr.clear()
    altura, largura = stdscr.getmaxyx()
    
    titulo = "Algoritmo de Criptografia com tabelas geradas de forma aleatória.\nSegurança de Redes - UPE: Matheus Robert\n\nEscolha uma opção:"
    stdscr.addstr(0, 0, titulo)

    primeira_linha_opcoes = 5  # Primeira linha para exibir as opções
    for idx, opcao in enumerate(opcoes):
        x = 0
        y = primeira_linha_opcoes + idx
        if idx == selecao:
            stdscr.attron(curses.color_pair(1))  # Ativa a cor azul (par de cores 1)
            opcao_exibida = "> " + opcao
            if len(opcao_exibida) > largura - 2 - x:
                opcao_exibida = opcao_exibida[:largura - 2 - x]
            stdscr.addstr(y, x, opcao_exibida)  # Alinha à esquerda com preenchimento
            stdscr.attroff(curses.color_pair(1))  # Desativa a cor azul
        else:
            opcao_exibida = "  " + opcao
            if len(opcao_exibida) > largura - 2 - x:
                opcao_exibida = opcao_exibida[:largura - 2 - x]
            stdscr.addstr(y, x, opcao_exibida)  # Alinha à esquerda com preenchimento

    stdscr.refresh()

def menu_principal(stdscr, opcoes):
    selecao = 0
    opcao = 0
    opcoes

    curses.curs_set(0)
    stdscr.keypad(True)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)  # Define a cor azul

    while True:
        exibir_menu(stdscr, opcoes, selecao)

        key = stdscr.getch()

        if key == curses.KEY_UP and selecao > 0:
            selecao -= 1
        elif key == curses.KEY_DOWN and selecao < len(opcoes) - 1:
            selecao += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if selecao == 0:
                opcao = 1
                break
            if selecao == 1:
                opcao = 2
                break
            if selecao == 2:
                sys.exit()     
                
    stdscr.keypad(False)
    curses.curs_set(1)
    return opcao

from rich.console import Console
from rich.table import Table
from rich import box


    
    
