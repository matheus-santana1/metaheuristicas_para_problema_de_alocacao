from src.leitor_de_instancias import ler_ordens, ler_equipes
from src.heuristicas_construtivas import heuristica_simples, heuristica_parcialmente_gulosa
from src.heuristica_de_alocacao import alocar_ordens
from src.grafico_de_gantt import plotar_grafico_gantt
from src.busca_local import busca_local_first_improvement
from src.grasp import grasp
from args import get_args
import logging
import sys

args = get_args()

def main():
    equipes = ler_equipes(args.equipes)
    ordens = ler_ordens(args.ordem)
    tipo_movimento = args.tipo_movimento #swap ou shift
    max_tempo_segundos = int(args.max_tempo_segundos)

    N = []
    if args.algoritmo == "simples":
        N = heuristica_simples(ordens)
    elif args.algoritmo == "parcialmente_gulosa":
        N = heuristica_parcialmente_gulosa(ordens)
    elif args.algoritmo == "grasp":
        return grasp(ordens, equipes, tipo_movimento, max_tempo_segundos, alpha=0.7)

    solucao = alocar_ordens(ordens, equipes, N)

    print(f"Solução inicial: {solucao}")

    if solucao.penalidade_total > 0:
        print("\nIniciando refinamento via Busca Local...")
        solucao = busca_local_first_improvement(ordens, equipes, solucao, tipo_movimento, max_tempo_segundos)
    else:
        print("\nBusca Local pulada (Solução já é ótima com penalidade 0).")

    print(f"Solução final: {solucao}\nTipo de movimento: {tipo_movimento}")
    return solucao

class Logger(object):
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log = open(filename, "w", encoding="utf-8")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        self.terminal.flush()
        self.log.flush()

if __name__ == "__main__":
    nome_arquivo_log = f"log_{args.arquivo}_{args.algoritmo}_{args.tipo_movimento}.txt"
    sys.stdout = Logger(nome_arquivo_log)
    solucao = main()
    if args.salvar_gantt:
        plotar_grafico_gantt(solucao, f"imagens/{args.arquivo}_heuristica_{args.algoritmo}")