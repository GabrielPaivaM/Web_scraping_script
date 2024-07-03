# ISSN Portal Data Scraper

Este script Python extrai dados do Portal ISSN de registros de pesquisas em vários países. Ele verifica se o registro já existe em um arquivo CSV e, se não, adiciona o novo registro ao arquivo.

## Funcionalidades

- 🔍 Extrai informações de registros de periódicos de vários países do Portal ISSN.
- ✔️ Verifica se o registro já existe no arquivo CSV antes de adicioná-lo.
- 💾 Armazena os registros no arquivo CSV `cnpq_data_portal_issn.csv`.

## Requisitos

- Python 3.x
- Bibliotecas Python:
  - `requests`
  - `beautifulsoup4`
  - `colorama`
  - `csv`

## Instalação

1. Clone o repositório para o seu ambiente local:

   ```bash
   git clone https://github.com/seu-usuario/issn-portal-data-scraper.git
   cd issn-portal-data-scraper
   ```

2. Instale as dependências:

   ```bash
   pip install requests bs4 colorama
   ```

3. Uso

   Execute esse script para cadastrar ou atualizar todos os dados no arquivo .csv (ele irá criar o arquivo .csv caso ainda não exista):

   ```bash
   python create_update_all.py
   ```

   O script começará a extrair dados do Portal ISSN e a registrar novos registros no arquivo CSV. Ele exibirá mensagens no console indicando o progresso.

   Execute esse script para atualizar todos os dados não cadastrados ainda no arquivo .csv (certifique-se de que o arquivo `cnpq_data_portal_issn.csv` existe no diretório e está corretamente formatado):

   ```bash
   python update_new.py
   ```

   O script começará a extrair dados do Portal ISSN e a registrar novos registros no arquivo CSV. Ele exibirá mensagens no console indicando o progresso.

   Execute esse script para informar a quantidade total de registros, listar os 5 primeiros e 5 últimos registros feitos no arquivo .csv (certifique-se de que o arquivo `cnpq_data_portal_issn.csv` existe no diretório e está corretamente formatado):

   ```bash
   python print_data.py
   ```

   O script exibirá a quantidade total de registros e listará os 5 primeiros e 5 últimos registros feitos no arquivo CSV.
