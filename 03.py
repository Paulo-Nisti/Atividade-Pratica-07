# Crie um script en Python que leia um arquivo CSV e exiba os dados na tela. 
# O arquivo CSV deve conter informações de pessoas, com colunas Nome, Idade e Cidade.


import csv
import os

# Nome do arquivo a ser lido
nome_arquivo = 'informacoes_pessoais.csv'

# Verifica se o arquivo existe antes de tentar abri-lo
if not os.path.exists(nome_arquivo):
    print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    print("Por favor, execute primeiro o script 'criar_csv.py' para gerar o arquivo.")
else:
    try:
        # Abre o arquivo para leitura ('r')
        # encoding='utf-8' é importante para ler acentos corretamente
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            
            # Cria um objeto "leitor" de CSV
            leitor_csv = csv.reader(f)
            
            # Pula a primeira linha (cabeçalho)
            try:
                cabecalho = next(leitor_csv)
                print(f"--- Lendo dados de '{nome_arquivo}' ---")
                print(f"Cabeçalho: {cabecalho}\n")
            except StopIteration:
                print("Arquivo está vazio.")
                cabecalho = None

            # Itera sobre as linhas restantes (dados)
            if cabecalho:
                contador_linhas = 0
                for linha in leitor_csv:
                    # 'linha' é uma lista de strings, ex: ['Ana Silva', '28', 'São Paulo']
                    print(f"Registro {contador_linhas + 1}:")
                    print(f"  {cabecalho[0]}: {linha[0]}") # Nome
                    print(f"  {cabecalho[1]}: {linha[1]}") # Idade
                    print(f"  {cabecalho[2]}: {linha[2]}") # Cidade
                    print("-" * 20) # Separador
                    contador_linhas += 1
                
                print(f"\nTotal de {contador_linhas} registros de dados lidos.")

    except IOError as e:
        print(f"Erro de E/S ao tentar ler o arquivo: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")