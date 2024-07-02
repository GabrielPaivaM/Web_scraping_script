import csv

from colorama import Fore

with open('cnpq_data_portal_issn.csv', 'r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    registers = list(reader)

# Exibe os 5 primeiros e os 5 ultimos registros.
if len(registers) > 0:
    i = 1
    j = len(registers) - 4
    for register in registers[:5]:
        print(f'{Fore.LIGHTGREEN_EX}[{i}] {Fore.LIGHTWHITE_EX}{register[0].split(";")[0]}{Fore.RESET}')
        i += 1

    print(f'{Fore.LIGHTYELLOW_EX}...')

    if len(registers) > 5:
        for register in registers[-5:]:
            print(f'{Fore.LIGHTGREEN_EX}[{j}] {Fore.LIGHTWHITE_EX}{register[0].split(";")[0]}{Fore.RESET}')
            j += 1

    print(f'{Fore.LIGHTWHITE_EX}Total de registros: {Fore.LIGHTYELLOW_EX}{len(registers)}{Fore.RESET}')

elif len(registers) == 5:
    i = 1
    for register in registers[:5]:
        print(f'[{i}] {register[0].split(";")[0]}')
        i += 1

    print(f'{Fore.LIGHTWHITE_EX}Total de registros: {Fore.LIGHTYELLOW_EX}{len(registers)}{Fore.RESET}')
else:
    print(f'{Fore.LIGHTRED_EX}Nenhum registro encontrado.{Fore.RESET}')