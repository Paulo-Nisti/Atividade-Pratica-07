# Crie um script em Python que leia e escreva dados em um arquivo JSON. 
# O arquivo JSON deve conter informações de uma pessoa, com campos nome, idade e cidade.


import json
import os

# Define o nome do arquivo
nome_arquivo = 'pessoa.json'

# --- 1. ESCRITA NO ARQUIVO JSON ---

# Dados da pessoa que vamos escrever
dados_pessoa = {
    "nome": "Carlos Santana",
    "idade": 42,
    "cidade": "Recife",
    "ativo": True,
    "habilidades": ["Python", "Engenharia de Dados", "Musica"]
}

print(f"--- 1. Escrevendo dados em '{nome_arquivo}' ---")
try:
    # Abre o arquivo em modo de escrita ('w')
    # 'encoding='utf-8'' garante que acentos sejam salvos corretamente
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        
        # json.dump() serializa o dicionário Python e o escreve no arquivo
        # indent=4 - Formata o JSON de forma legível (pretty-print)
        # ensure_ascii=False - Permite a escrita de caracteres acentuados (ex: "Recife")
        json.dump(dados_pessoa, f, indent=4, ensure_ascii=False)

    print(f"Os seguintes dados foram escritos com sucesso:")
    print(json.dumps(dados_pessoa, indent=2, ensure_ascii=False))
    print("-" * 30)

except IOError as e:
    print(f"Erro de E/S ao escrever o arquivo: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado na escrita: {e}")


# --- 2. LEITURA DO ARQUIVO JSON ---

print(f"\n--- 2. Lendo dados de '{nome_arquivo}' ---")

# Verifica se o arquivo realmente existe
if not os.path.exists(nome_arquivo):
    print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
else:
    try:
        # Abre o arquivo em modo de leitura ('r')
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            
            # json.load() lê o arquivo e desserializa o JSON
            # de volta para um objeto Python (neste caso, um dicionário)
            dados_lidos = json.load(f)

        print("Dados lidos com sucesso!\n")
        
        # Exibe os dados lidos acessando as chaves do dicionário
        print("Conteúdo lido do arquivo:")
        print(f"  Nome: {dados_lidos.get('nome')}")
        print(f"  Idade: {dados_lidos.get('idade')}")
        print(f"  Cidade: {dados_lidos.get('cidade')}")
        print(f"  Ativo: {dados_lidos.get('ativo')}")
        
        # Acessando um item da lista
        if 'habilidades' in dados_lidos and dados_lidos['habilidades']:
            print(f"  Habilidade principal: {dados_lidos['habilidades'][0]}")
        
        print("-" * 30)

    except json.JSONDecodeError:
        print(f"Erro: O arquivo '{nome_arquivo}' não contém um JSON válido.")
    except IOError as e:
        print(f"Erro de E/S ao ler o arquivo: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado na leitura: {e}")