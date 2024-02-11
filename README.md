# Projeto de Criptografia com Chaves

Este é um projeto que visa traduzir texto para formato binário utilizando tabelas de tradução carregadas de arquivos CSV. Abaixo estão as principais informações sobre o projeto:

### Funcionalidades

1. **`translater_tabs.py`**: Este módulo contém funções para carregar tabelas de tradução de um arquivo CSV e usar essas tabelas para traduzir texto para formato binário.

2. **`gen_tables.py`**: Neste módulo, são definidas funções para gerar tabelas aleatórias para uso na tradução para binário.

3. **`tradutor.py`**: Aqui estão implementadas funções para traduzir texto de formato binário de volta para texto normal.

4. **`cripto_translater.py`**: Este módulo possui funções para carregar tabelas de tradução a partir de arquivos CSV e traduzir texto para formato binário usando essas tabelas.

5. **`funcoes.py`**: Contém funções auxiliares utilizadas em todo o projeto, como limpeza de console e exibição de menus.

6. **`main.py`**: O arquivo principal do projeto, que fornece uma interface para o usuário interagir com as funcionalidades implementadas.

### Como Usar

Para utilizar este projeto, siga os passos abaixo:

1. Certifique-se de ter instalado todas as dependências necessárias, que estão listadas no arquivo `requirements.txt`. Você pode instalar essas dependências usando o comando `pip install -r requirements.txt`.

2. Execute o arquivo `main.py`. Isso iniciará o programa e você será apresentado com um menu onde pode escolher entre escrever uma mensagem para ser traduzida ou traduzir um arquivo.

3. Se optar por escrever uma mensagem, o programa pedirá que você digite o texto. Em seguida, será solicitado que escolha se deseja salvar a mensagem traduzida em um arquivo ou apenas exibi-la na tela.

4. Se optar por traduzir um arquivo, o programa pedirá que você digite o nome do arquivo. O conteúdo do arquivo será traduzido para texto normal e exibido na tela.

### Estrutura do Projeto

A estrutura de diretórios do projeto é a seguinte:

```
- main.py
- funcoes.py
- translater_tabs.py
- gen_tables.py
- tradutor.py
- cripto_translater.py
- readme.md
```
