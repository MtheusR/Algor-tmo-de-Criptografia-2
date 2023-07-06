import csv, gen_tables, cripto_translater


def translate_binary_to_text(binary_text):
    text = ""
    n_tabelas_tabs = get_table_sizes('tabs.csv', 0)
    n_tabelas_key = get_table_sizes('key.csv', 1)
    
    while len(binary_text) >= n_tabelas_tabs:
        binary_chars_tab = binary_text[:n_tabelas_tabs]
        remaining_text = binary_text[n_tabelas_tabs:]

        translation_table_tabs = cripto_translater.load_translation_tables("tabs.csv")
        translation_table_key = cripto_translater.load_translation_tables("key.csv")

        found_tab_translation = False
        for translation_table_tabs in translation_table_tabs:
            for character, binary_value in translation_table_tabs.items():
                if binary_value == binary_chars_tab:
                
                    found_tab_translation = True
                    break
            if found_tab_translation:
                break
            
        n_char_key = n_tabelas_key[int(character)]

        if len(remaining_text) >= n_char_key:
            binary_chars_key = remaining_text[:n_char_key]
            remaining_text = remaining_text[n_char_key:]

            found_key_translation = False
            for translation_table_key in translation_table_key:
                for character, binary_value in translation_table_key.items():
                    if binary_value == binary_chars_key:
                        text += character
                        found_key_translation = True
                        break
                if found_key_translation:
                    break

        binary_text = remaining_text

    return text

def get_table_sizes(csv_file, tipo):
    table_sizes = []

    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Ler a primeira linha do arquivo CSV (cabeçalho)
        for column_index in range(1, len(header)):
            table_size = 0
            file.seek(0)  # Reiniciar a leitura do arquivo para cada tabela
            next(reader)  # Ignorar a primeira linha novamente
            for row in reader:
                if column_index < len(row):  # Verificar se o índice é válido na lista row
                    binary_value = row[column_index]
                    table_size = max(table_size, len(binary_value))
            table_sizes.append(table_size)

    if tipo == 0:
        return max(table_sizes)
    else:
        return table_sizes
