from src.busca_local import busca_local_first_improvement
from src.heuristicas_construtivas import heuristica_parcialmente_gulosa
from src.heuristica_de_alocacao import alocar_ordens
import time

def grasp(ordens, equipes, tipo_movimento, max_tempo_segundos=300, alpha=0.7):
    inicio_total = time.time()
    melhor_solucao_global = None
    iteracao = 0
    print(f"=== Iniciando GRASP (Max Tempo: {max_tempo_segundos}s, Alpha: {alpha}) ===")

    while (time.time() - inicio_total) < max_tempo_segundos:
        iteracao += 1
        tempo_restante = max_tempo_segundos - (time.time() - inicio_total)

        N_candidato = heuristica_parcialmente_gulosa(ordens, alpha)
        solucao_inicial = alocar_ordens(ordens, equipes, N_candidato)

        # Limite de tempo para a busca local, Maximo de 10% do tempo de total
        tempo_limite_busca = min(tempo_restante, max_tempo_segundos/6)
        solucao_refinada = busca_local_first_improvement(
            ordens,
            equipes,
            solucao_inicial,
            tipo_movimento,
            max_tempo_segundos=tempo_limite_busca
        )

        if melhor_solucao_global is None or solucao_refinada.penalidade_total < melhor_solucao_global.penalidade_total:
            melhor_solucao_global = solucao_refinada
            print(f"\n[*] NOVA MELHOR SOLUÇÃO NA ITERAÇÃO {iteracao}!")
            print(f"    Penalidade: {melhor_solucao_global.penalidade_total}")
            print(f"    Alocadas: {len(melhor_solucao_global.ordens_alocadas)}")

        if iteracao % 5 == 0:
            print(
                f"... GRASP rodando. Iteração {iteracao}. Melhor Penalidade: {melhor_solucao_global.penalidade_total}")

    print(f"\n=== FIM GRASP ===")
    print(f"Total Iterações: {iteracao}")
    print(f"Melhor Penalidade Encontrada: {melhor_solucao_global.penalidade_total}")
    return melhor_solucao_global