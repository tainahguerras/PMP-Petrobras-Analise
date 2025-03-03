import re

# Lista com urls de compartilhamento do Google Sheets
urls = [
    'https://docs.google.com/spreadsheets/d/1R78gxRyUJsti8iOQT_VYUdqKj12kGWFXWqgmZk6Xuj0/edit?usp=sharing',
    'https://docs.google.com/spreadsheets/d/14zxZYPrRbb6FP7xJcgK52cT2HEjZx5g6rAPsY2n36wo/edit?usp=sharing',
    'https://docs.google.com/spreadsheets/d/15P7w_jzUVY18t0-gDz5cmHpY7Xf-5pMo8BTh3QZwjVU/edit?usp=sharing',
    'https://docs.google.com/spreadsheets/d/1DeuecMTI8ySMd5xN-5HEtB3N8wOVaoZl3ARnLLUMwFQ/edit?usp=sharing',
    'https://docs.google.com/spreadsheets/d/1bIJSCOSpXaewZiqFlPAExoRpu3jHevQk32n8ws8Q8vE/edit?usp=sharing',
    'https://docs.google.com/spreadsheets/d/1-DAMcsRODfJgQF4HJPT_kVKYxS3Tamd9Fuxzo2wrslo/edit?usp=sharing'
]

# Lista com nomes dos dataframes
nomes_dataframes = ['BC_ES', 'BS_SC_PR', 'BS_SP', 'BS_RJ', 'RN_CE', 'SE_AL']

# Converte urls de compartilhamento do Google Sheets para serem lidas pelo pandas
def conversor_url(url):
   
    padrao = r'https://docs\.google\.com/spreadsheets/d/([a-zA-Z0-9-_]+)(/edit#gid=(\d+)|/edit.*)?'
    substituicao = lambda m: f'https://docs.google.com/spreadsheets/d/{m.group(1)}/export?' + (f'gid={m.group(3)}&' if m.group(3) else '') + 'format=csv'
    nova_url = re.sub(padrao, substituicao, url)

    return nova_url

# Calcula a porcentagem de valores nulos de uma coluna em um dataframe
def calcular_porcentagem_nulos(df, nome, coluna):
    total_linhas = len(df)
    total_nulos = df[coluna].isnan().sum()
    porcentagem_nulos = (total_nulos / total_linhas) * 100
    print(f"{nome}: {porcentagem_nulos:.2f}% de valores ausentes")