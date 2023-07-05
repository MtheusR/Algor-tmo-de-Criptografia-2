import cripto_translater 

input_text = input("Digite um texto: ")
translation = cripto_translater.translate_text(input_text, cripto_translater.load_translation_tables('key.csv'))
    
print(translation)