import argparse
from src.leitor_de_instancias import ler_ordens, ler_equipes
from src.heuristicas_construtivas import heuristica_simples, heuristica_por_ferramenta
from src.heuristica_de_alocacao import alocar_ordens
from src.grafico_de_gantt import plotar_grafico_gantt


def main():
    parser = argparse.ArgumentParser(description="Leitor de equipes e ordens de manutenção.")
    parser.add_argument("--equipes", required=True, help="Caminho para o arquivo de equipes (.csv)")
    parser.add_argument("--ordem", required=True, help="Caminho para o arquivo de ordens (.csv)")

    args = parser.parse_args()

    equipes = ler_equipes(args.equipes)
    ordens = ler_ordens(args.ordem)

    N = heuristica_por_ferramenta(ordens)
    solucao, penalidade = alocar_ordens(ordens, equipes, N)

    print("\n=== Alocações ===")
    for s in solucao.ordens_alocadas:
        print(s)

    print(f"\nPenalidade total: {penalidade}")
    print("Ordens não alocadas:", [o.id for o in solucao.ordens_nao_alocadas])

    plotar_grafico_gantt(solucao)


if __name__ == "__main__":
    main()
