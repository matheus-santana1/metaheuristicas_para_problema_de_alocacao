import argparse
import random


def get_args():
    parser = argparse.ArgumentParser(description="Leitor de equipes e ordens de manutenção.")
    parser.add_argument("--equipes", required=True, help="Caminho para o arquivo de equipes (.csv).")
    parser.add_argument("--ordem", required=True, help="Caminho para o arquivo de ordens (.csv).")
    parser.add_argument("--seed", required=False, help="Semente para função random.")
    seed = parser.parse_args().seed
    if seed:
        random.seed(int(seed))
    return parser.parse_args()
