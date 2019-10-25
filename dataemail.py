import os
import re
import csv

from pathlib import Path

def gera_dataset ():
    # nome das colunas para setar no cvs
    csv_columns = ['conteudo','fraude']

    #dicionário contento as chaves e valores que farão parter do csv
    dict_emails = {'conteudo':'', 'fraude': 0}

    # Lista todos os arquivos no diretóro usando o pathlib
    basepath = Path('emails/') # Diretório dos arquivos

    # Retorna a lista de arquivos
    files_in_basepath = (file for file in basepath.iterdir() if file.is_file())
    
    # Abre/cria o arquivo dataset em modo escrita
    data_file = open('dataset.csv', 'w')

    # Percorre a lista de arquivos
    for item in files_in_basepath:
        
        #Pega o caminho e o nome de cada aquivo
        arquivo = 'emails/' + item.name
        print('Lendo arquivo' + arquivo)
        
        # Abre o arquivo atual
        f = open(arquivo)

        # Lê o arquivo atual e 
        # remove o cabeçalho que não será utilizado
        # pegando somemente o conteudo
        fr = re.sub('.*:.*','', f.read())

        # seta os valores (as mensagens) no campo conteudo 
        dict_emails['conteudo'] = fr

        # prepara o csv para receber os valores do dicionario
        # com o nome das colunas
        writer = csv.DictWriter(data_file, fieldnames=csv_columns)
        writer.writeheader()

        # escreve no arquivo dataset.csv com os dados do dicionário
        writer.writerow(dict_emails)
    # fecha o arquivo dataset.csv    
    data_file.close()


gera_dataset()
