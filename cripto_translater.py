import csv, translater_tabs

def load_translation_tables(csv_file):
    translation_tables = []
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Ler a primeira linha do arquivo CSV (cabeçalho)
        for column_index in range(1, len(header)):
            translation_table = {}
            file.seek(0)  # Reiniciar a leitura do arquivo para cada tabela
            next(reader)  # Ignorar a primeira linha novamente
            for row in reader:
                if len(row) >= 1:  # Verificar se a lista row possui elementos
                    character = row[0]
                    binary_value = row[column_index] if column_index < len(row) else ""
                    translation_table[character] = binary_value
            translation_tables.append(translation_table)
    return translation_tables

def translate_text(text, translation_tables):
    translation = ""
    character_count = {}
    for char in text:
        if char not in character_count:
            character_count[char] = 1
        else:
            character_count[char] += 1
            
        table_index = character_count[char] - 1
        if table_index >= len(translation_tables):
            table_index = table_index % len(translation_tables)
        translation_table = translation_tables[table_index]         

        tabelas_de_traducao = translater_tabs.carregar_tabelas_de_traducao('tabs.csv')
        tabs = translater_tabs.obter_tabs(str(table_index), tabelas_de_traducao)
        
        if char in translation_table:
            binary_value = translation_table[char]
            translation += tabs + binary_value
            
    return translation.strip()

def load_key_csv(csv_file):
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        return list(reader)