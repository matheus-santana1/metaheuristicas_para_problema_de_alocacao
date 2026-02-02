from src.leitor_de_instancias import ler_ordens, ler_equipes
from src.heuristicas_construtivas import heuristica_simples, heuristica_parcialmente_gulosa
from src.heuristica_de_alocacao import alocar_ordens
from src.grafico_de_gantt import plotar_grafico_gantt
from src.busca_local import busca_local_first_improvement
from args import get_args

args = get_args()

def main():
    equipes = ler_equipes(args.equipes)
    ordens = ler_ordens(args.ordem)
    tipo_movimento = args.tipo_movimento #swap ou shift

    N = []
    if args.tipo_heuristica == "simples":
        N = heuristica_simples(ordens)
    elif args.tipo_heuristica == "parcialmente_gulosa":
        N = heuristica_parcialmente_gulosa(ordens)

    solucao = alocar_ordens(ordens, equipes, N)

    print(f"Solução inicial: {solucao}")

    if solucao.penalidade_total > 0:
        print("\nIniciando refinamento via Busca Local...")
        solucao = busca_local_first_improvement(ordens, equipes, solucao, tipo_movimento)
    else:
        print("\nBusca Local pulada (Solução já é ótima com penalidade 0).")

    print(f"Solução final: {solucao}\nTipo de movimento: {tipo_movimento}")
    return solucao

if __name__ == "__main__":
    solucao = main()
    plotar_grafico_gantt(melhor_solucao, f"imagens/{args.arquivo}_heuristica_{args.tipo_heuristica}")