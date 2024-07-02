import requests
from bs4 import BeautifulSoup
import time

import csv

from colorama import Fore, Style, init

url = 'https://portal.issn.org/api/search/?q=api%2Fsearch&search%5B0%5D=MUST%3Dcountry%3DAIA%2CATG%2CARG%2CABW%2CBHS%2CBRB%2CBLZ%2CBOL%2CBES%2CBRA%2CCYM%2CCHL%2CCOL%2CCRI%2CCUB%2CCUW%2CDMA%2CDOM%2CECU%2CSLV%2CGNQ%2CGUF%2CGRD%2CGLP%2CGTM%2CGUY%2CHTI%2CHND%2CJAM%2CMTQ%2CMEX%2CMSR%2CNIC%2CPAN%2CPRY%2CPER%2CPRI%2CMAF%2CVCT%2CSUR%2CTTO%2CURY%2CVEN&search%5B1%5D=MUST%3Drecord%3DRegister&search%5B2%5D=MUST_EXIST%3Droadindex&role%5B0%5D=11&search_id=38321820&size=100&currentpage=1'

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')

# Pega o numero de paginas existentes
last_page = soup.find('p', class_="pagination-mobile-notices-count").get_text().strip()
number_of_last_page = last_page[(last_page.find('/')) + 1 : last_page.find('P')]

total_start_time = time.time()

# Armazena os tempos gastos em cada pagina para calcular a media posteriormente.
list_of_times = []

# É usada para verificar se uma pagina foi salva com sucesso.
success = 0

# Conta quantas paginas foram salvas com sucesso.
success_count = 0

# Conta qual pesquisa esta sendo registrada.
c = 1

# Abre o arquivo em modo escrita para sobrescrever o conteudo ja existente, se não tiver um arquivo ele cria um novo.
with open('cnpq_data_portal_issn.csv', 'w', newline='', encoding='UTF-8') as f:

    for i in range(1, int(number_of_last_page) + 1):
        start_time_page = time.time()
        url_page = f'https://portal.issn.org/api/search/?q=api%2Fsearch&search%5B0%5D=MUST%3Dcountry%3DAIA%2CATG%2CARG%2CABW%2CBHS%2CBRB%2CBLZ%2CBOL%2CBES%2CBRA%2CCYM%2CCHL%2CCOL%2CCRI%2CCUB%2CCUW%2CDMA%2CDOM%2CECU%2CSLV%2CGNQ%2CGUF%2CGRD%2CGLP%2CGTM%2CGUY%2CHTI%2CHND%2CJAM%2CMTQ%2CMEX%2CMSR%2CNIC%2CPAN%2CPRY%2CPER%2CPRI%2CMAF%2CVCT%2CSUR%2CTTO%2CURY%2CVEN&search%5B1%5D=MUST%3Drecord%3DRegister&search%5B2%5D=MUST_EXIST%3Droadindex&role%5B0%5D=11&search_id=38321820&size=100&currentpage={i}'
        site = requests.get(url_page, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        articles = soup.find_all('div', class_="item-result-block")

        for article in articles:
            start_time_article = time.time()
            if article:

                title = article.find('h5', class_="item-result-title").get_text().strip()

                if not title:
                    title = "Titulo não informado"

                # Lista para armazenar os textos dos parágrafos.
                paragraph_texts = []

                content_divs = article.find_all('div', class_="item-result-content-text flex-zero")

                for content_div in content_divs:
                    paragraphs = content_div.find_all('p')

                    for p in paragraphs:
                        if 'text-center hidden-tablet selectMobile' not in p.get('class', []) and p.find('label', class_="btn btn-item-select") is None:

                            # Verifica se há um link no paragrafo.
                            link = p.find('a')
                            if link and 'href' in link.attrs:
                                url_complete = link['href'].strip()
                                if not url_complete:
                                    paragraph_texts.append('Não informado')
                                else:
                                    paragraph_texts.append(f'URL:{url_complete}')
                            else:
                                paragraph_text = p.get_text(strip=True)
                                if not paragraph_text:
                                    paragraph_text = "Não informado"
                                paragraph_texts.append(paragraph_text)

                    line = "Title: " + title + ";"
                    for text in paragraph_texts:
                        line += " " + text + ";"
                    line += "\n"

                    elapsed_time = time.time() - start_time_article

                    f.write(line)
                    print(f'{Fore.LIGHTGREEN_EX}Pesquisa {Fore.LIGHTWHITE_EX}{c}{Fore.LIGHTGREEN_EX} na pagina {Fore.LIGHTWHITE_EX}{i}{Fore.LIGHTGREEN_EX} registrada com sucesso em {Fore.LIGHTWHITE_EX}{elapsed_time:.3f}{Fore.LIGHTGREEN_EX} segundos.\n')
                    c += 1
                    success = 1
            else:
                print(f'{Fore.LIGHTRED_EX}Nenhuma pesquisa encontrada na pagina {Fore.LIGHTWHITE_EX}{i}.\n')

        elapsed_time_page = time.time() - start_time_page
        if success == 1:
            list_of_times.append(elapsed_time_page)
            success_count += 1

total_elapsed_time = time.time() - total_start_time

# Calcula a media de tempo gasto por pagina.
if success_count > 0:
    timem = sum(list_of_times)
    medium_time = timem / success_count
else:
    medium_time = 0

print(f'{Fore.LIGHTWHITE_EX}O tempo total gasto foi de {Fore.LIGHTYELLOW_EX}{total_elapsed_time:.2f}{Fore.LIGHTWHITE_EX} segundos com um tempo medio de {Fore.LIGHTYELLOW_EX}{medium_time:.2f}{Fore.LIGHTWHITE_EX} segundos por pagina.{Fore.WHITE}')