import re

# Listas

## lista com urls de compartilhamento público do Google Sheets dos datasets utilizados no projeto
urls = [
    'https://docs.google.com/spreadsheets/d/1EHm8Mz1Q6x4LG_3nN0EkXQgNCBFagWTrDmsl4qxqBRI/edit?usp=sharing',
    'https://docs.google.com/spreadsheets/d/131TJcc4uMB148_PNGfsDCvT-w3unLBNdMIQBtWoYM-E/edit?usp=sharing',
    'https://docs.google.com/spreadsheets/d/17nFHmie9GRr2n7TbZynW_a-fBiu13PoGGeYuXfwQfcM/edit?usp=sharing',
    'https://docs.google.com/spreadsheets/d/1DGOvV0OJF6XNbK-BZG91v3WFw3_K2mjKZGmnsk0Xs1I/edit?usp=sharing',
    'https://docs.google.com/spreadsheets/d/1XR8esB6C7quAOiF1jSfygIh_YwbwGLSL0FE1LZ_UAII/edit?usp=sharing',
    'https://docs.google.com/spreadsheets/d/1tJv5OOb_QSpcl15ij516pyX5KuL-gReCNV6KfujuIpg/edit?usp=sharing'
]

## lista de colunas previamente selecionadas para análise exploratória
colunas_selecionadas = ['Código', 'Identificador do indivíduo', 'Instituição executora', 'Estado', 'Cidade', 'Praia', 'Trecho', 'Estratégia do trecho', 'Maré inicial', 'Vento inicial', 'Tipo do monitoramento', 'Data/Hora', 'Ponto - Lat', 'Ponto - Long', 'Espécies - Classe', 'Espécies - Ordem', 'Espécies - Subordem', 'Espécies - Família', 'Espécies - Gênero', 'Espécies - Espécie', 'Espécie ameaçada', 'Caracterização do ambiente', 'Condição']

# Funções

## converte urls de compartilhamento do Google Sheets em formato correto para serem lidas pelo Pandas
def conversor_url(url):
   
    padrao = r'https://docs\.google\.com/spreadsheets/d/([a-zA-Z0-9-_]+)(/edit#gid=(\d+)|/edit.*)?'
    substituicao = lambda m: f'https://docs.google.com/spreadsheets/d/{m.group(1)}/export?' + (f'gid={m.group(3)}&' if m.group(3) else '') + 'format=csv'
    nova_url = re.sub(padrao, substituicao, url)

    return nova_url

## calcula a porcentagem de valores nulos de uma coluna em um dataframe
def calcular_porcentagem_nulos(df, nome, coluna):
    total_nulos = df[coluna].isnull().sum()
    porcentagem_nulos = (total_nulos / len(df)) * 100
    print(f"{nome}: {porcentagem_nulos:.2f}% de valores ausentes")