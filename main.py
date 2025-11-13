from src.leitor_de_instancias import ler_ordens, ler_equipes
from src.heuristicas_construtivas import heuristica_simples, heuristica_parcialmente_gulosa
from src.heuristica_de_alocacao import alocar_ordens
from src.grafico_de_gantt import plotar_grafico_gantt
from args import get_args


def main():
    args = get_args()

    equipes = ler_equipes(args.equipes)
    ordens = ler_ordens(args.ordem)

    N = heuristica_parcialmente_gulosa(ordens)
    solucao = alocar_ordens(ordens, equipes, N)

    print(solucao)

    print("\n=== Alocações ===")
    for s in solucao.ordens_alocadas:
        print(s)

    print(f"\nPenalidade total: {solucao.penalidade_total}")
    print("Ordens não alocadas:", [o.id for o in solucao.ordens_nao_alocadas])

    plotar_grafico_gantt(solucao)


if __name__ == "__main__":
    main()
