import argparse
import random


def get_args():
    parser = argparse.ArgumentParser(description="Leitor de equipes e ordens de manutenção.")
    parser.add_argument("--equipes", required=True, help="Caminho para o arquivo de equipes (.csv).")
    parser.add_argument("--ordem", required=True, help="Caminho para o arquivo de ordens (.csv).")
    parser.add_argument("--arquivo", required=True, help="Nome do arquivo gerado da solução (.png).")
    parser.add_argument("--algoritmo", required=True, help="Tipo de heurística a ser usada.")
    parser.add_argument("--tipo_movimento", required=True, help="Tipo de movimento a ser usado.")
    parser.add_argument("--seed", required=False, help="Semente para função random.")
    parser.add_argument("--max_tempo_segundos", required=True, help="Tempo máximo para execução do GRASP ou Busca Local.")
    parser.add_argument("--salvar_gantt", action="store_true", help="Se presente, salva o gráfico de GANTT.")
    seed = parser.parse_args().seed
    if seed:
        random.seed(int(seed))
    return parser.parse_args()
