# Leia um arquivo que contenha dados de log de treinamento de modelos de Machine Learning. 
# Calcule a média e o desvio padrão do tempo de exercução constantes.

import re
import statistics
import os

def analisar_log(filepath):
    """
    Lê um arquivo de log, extrai os tempos de execução e calcula
    a média e o desvio padrão.
    """
    # Lista para armazenar todos os tempos de execução encontrados
    tempos_execucao = []
    
    # Expressão regular para encontrar o padrão "Tempo de Execucao: XXX.Xs"
    # \d+ -> um ou mais dígitos
    # \.   -> um ponto literal
    # (\d+\.\d+) -> captura o grupo de números (ex: 304.2)
    padrao = re.compile(r"Tempo de Execucao: (\d+\.\d+)s")
    
    # Verifica se o arquivo existe
    if not os.path.exists(filepath):
        print(f"Erro: O arquivo '{filepath}' não foi encontrado.")
        return

    print(f"Analisando o arquivo: {filepath}\n")
    
    # Abre e lê o arquivo linha por linha
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for linha in f:
                # Procura o padrão na linha atual
                match = padrao.search(linha)
                
                # Se o padrão for encontrado...
                if match:
                    # Extrai o valor capturado (grupo 1) e converte para float
                    tempo_str = match.group(1)
                    tempos_execucao.append(float(tempo_str))

    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
        return

    # Calcula as estatísticas
    if not tempos_execucao:
        print("Nenhum dado de 'Tempo de Execucao' foi encontrado no log.")
        return

    # Calcula a média
    media = statistics.mean(tempos_execucao)
    
    # Calcula o desvio padrão (requer pelo menos 2 pontos de dados)
    desvio_padrao = 0.0
    if len(tempos_execucao) > 1:
        desvio_padrao = statistics.stdev(tempos_execucao)
    
    # Imprime os resultados
    print("--- Resultados da Análise ---")
    print(f"Total de amostras (épocas): {len(tempos_execucao)}")
    print(f"Tempos encontrados (s): {tempos_execucao}")
    print("--- Estatísticas ---")
    print(f"Média: {media:.2f}s")
    print(f"Desvio Padrão: {desvio_padrao:.2f}s")

# --- Ponto de entrada do script ---
if __name__ == "__main__":
    # Define o nome do arquivo de log que está no mesmo diretório
    nome_arquivo_log = 'log.txt'
    
    # Chama a função de análise
    analisar_log(nome_arquivo_log)