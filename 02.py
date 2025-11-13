# Crie um script em Python que escreva dados em um arquivo CSV. 
# O arquivo CSV deve conter informações pessoais, como colunas Nome, Idade e Cidade.


import csv
import os

# Define o nome do arquivo a ser criado
nome_arquivo = 'informacoes_pessoais.csv'

# 1. Define os cabeçalhos (colunas)
cabecalhos = ['Nome', 'Idade', 'Cidade']

# 2. Define os dados (linhas)
dados = [
    ['Ana Silva', 28, 'São Paulo'],
    ['Bruno Costa', 45, 'Rio de Janeiro'],
    ['Carla Mendes', 32, 'Belo Horizonte'],
    ['Daniel Moreira', 19, 'Salvador'],
    ['Elisa Fernandes', 51, 'Curitiba'],
    ['João Almeida', 37, 'Fortaleza'] # Exemplo com acentuação
]

# 3. Escreve no arquivo CSV
try:
    # 'w' = modo de escrita (write). Cria o arquivo se não existir, 
    # ou sobrescreve se já existir.
    # newline='' - Essencial para a escrita correta de CSV.
    # encoding='utf-8' - Garante a gravação correta de acentos.
    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as f:
        
        # Cria um objeto "escritor" de CSV
        escritor_csv = csv.writer(f)
        
        # Escreve a linha de cabeçalho
        escritor_csv.writerow(cabecalhos)
        
        # Escreve todas as linhas de dados de uma vez
        escritor_csv.writerows(dados)

    print(f"Arquivo '{nome_arquivo}' foi criado com sucesso!")
    print(f"Localização: {os.path.abspath(nome_arquivo)}")

except IOError as e:
    print(f"Erro de E/S ao tentar escrever o arquivo: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")