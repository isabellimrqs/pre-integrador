#Arquivo XLSX
from bs4 import BeautifulSoup
import pandas as pd

file_path = 'T:/1DS-MB-B/Isabelli Maciel Marques/FPOO/MARCIA/formativa/FPOO-Formativa-WebScraping_E-commerce.html'

with open(file_path, 'r', encoding='utf-8') as file:
    conteudo_html = file.read()

soup = BeautifulSoup(conteudo_html, 'html.parser')

#Encontrar a tabela no HTML
tabela = soup.find('table')

#Verifica se encontrou a tabela
if tabela:
    #Extrai dados da tabela usando BeautifulSoup
    dados_tabela = []
    for row in tabela.find_all('tr'):
        dados_linha = [data.text for data in row.find_all(['td', 'th'])]
        dados_tabela.append(dados_linha)

    #Cria um DataFrame do Pandas com os dados da tabela
    df = pd.DataFrame(dados_tabela[1:], columns=dados_tabela[0])

    #Remove caracteres especiais para não dar erro no XML
    df.columns = df.columns.str.replace(' ', '_').str.replace('[^\w\s]', '', regex=True)

    #Salva o DataFrame em um arquivo Excel, Json e XML
    try:
        df.to_excel('pedidos.xlsx', index=False)
        print('Dados salvos no Excel.')
        df.to_json('pedidos.json', orient='records', lines=True)
        print('Dados salvos no JSON.')
        df.to_xml('pedidos.xml', index=False)
        print('Dados salvos no XML.')
        df.to_csv('pedidos.csv',index=False)
        print('Dados salvos no CSV.')
    except:
        print('Não foi possível salvar os dados.')

else:
    print('Nenhuma tabela encontrada no HTML.')


