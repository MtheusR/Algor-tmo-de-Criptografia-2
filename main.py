import cripto_translater, tradutor, gen_tables, funcoes
import string, os
 
if not os.path.isfile('key.csv') or not os.path.isfile('tabs.csv'):
    
    funcoes.print_files_main()
    
    n_tabelas_chaves = gen_tables.gerar_tamanho_tabelas(5, 10) 
    char_ascii = " " + string.ascii_letters + string.digits + string.punctuation 
    gen_tables.gerar_arquivo_csv('key', char_ascii, n_tabelas_chaves)
    funcoes.print_file('key.csv')


    num_tabelas_tabs = gen_tables.gerar_tamanho_tabelas_tabs(n_tabelas_chaves)
    char_tabs = list(range(len(num_tabelas_tabs)))
    gen_tables.gerar_arquivo_csv('tabs', char_tabs, num_tabelas_tabs)
    funcoes.print_file('tabs.csv')

    print("\nQuantidade - Tabelas Caracteres:", len(n_tabelas_chaves))
    print("Tamanho - Tabela Caracteres:", n_tabelas_chaves)
    print("Quantidade - Tabelas Separadores:", len(num_tabelas_tabs))
    print("Tamanho - Tabela Separadores: ", num_tabelas_tabs[0])
    
input_text = input("\nDigite um texto: ")
translation = cripto_translater.translate_text(input_text, cripto_translater.load_translation_tables('key.csv'))
    
print(translation)

text = tradutor.translate_binary_to_text(translation)
print("Texto traduzido:", text)
