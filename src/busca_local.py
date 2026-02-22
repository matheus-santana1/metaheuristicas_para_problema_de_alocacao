from src.heuristica_de_alocacao import alocar_ordens
import time

def tem_interseccao(ordem1, ordem2):
    """
    Verifica se duas ordens possuem janelas de tempo conflitantes.
    Matematicamente: max(inicio1, inicio2) <= min(fim1, fim2)
    """
    inicio_max = max(ordem1.inicio, ordem2.inicio)
    fim_min = min(ordem1.fim, ordem2.fim)
    return inicio_max <= fim_min


def busca_local_first_improvement(ordens, equipes, solucao_inicial, tipo_movimento, max_tempo_segundos):
    """
    Busca Local First Improvement OTIMIZADA.

    Otimizações aplicadas:
    1. Foco nas Não Alocadas: O loop principal itera apenas sobre as ordens que
       geram penalidade (não alocadas).
    2. Poda por Interseção: Só testa troca se houver conflito de janela.
    """
    inicio_execucao = time.time()

    melhor_solucao = solucao_inicial
    melhor_penalidade = solucao_inicial.penalidade_total
    melhor_N = list(solucao_inicial.N)
    if max_tempo_segundos is None:
        max_tempo_segundos = len(melhor_N)
    melhorou = True
    iteracao = 0

    print(f"--- Iniciando Busca Local Otimizada (Penalidade Inicial: {melhor_penalidade}) ---")
    while melhorou:
        if (time.time() - inicio_execucao) > max_tempo_segundos:
            print(f"!!! Tempo limite de {max_tempo_segundos}s atingido !!!")
            break

        melhorou = False
        tamanho_N = len(melhor_N)


        ids_nao_alocados = {o.id for o in melhor_solucao.ordens_nao_alocadas}
        indices_foco = [i for i, ordem in enumerate(melhor_N) if ordem.id in ids_nao_alocados]
        if not indices_foco:
            break

        trocas_avaliadas = 0
        trocas_efetivas = 0

        for i in indices_foco:
            if melhorou: break
            ordem_i = melhor_N[i]
            for j in range(tamanho_N):
                if i == j: continue

                if (time.time() - inicio_execucao) > max_tempo_segundos: break

                ordem_j = melhor_N[j]
                trocas_avaliadas += 1

                if not tem_interseccao(ordem_i, ordem_j):
                    continue

                trocas_efetivas += 1


                # --- Movimento: SWAP ou SHIFT ---
                vizinho_N = list(melhor_N)
                if tipo_movimento == "swap":
                    vizinho_N[i], vizinho_N[j] = vizinho_N[j], vizinho_N[i]
                elif tipo_movimento == "shift":
                    ordem_removida = vizinho_N.pop(i)
                    vizinho_N.insert(j, ordem_removida)

                nova_solucao = alocar_ordens(ordens, equipes, vizinho_N)

                # Critério de Aceitação (First Improvement)
                if nova_solucao.penalidade_total < melhor_penalidade:
                    diff = melhor_penalidade - nova_solucao.penalidade_total
                    print(
                        f"  > [Iter {iteracao}] MELHORA! (-{diff}) Trocando ordem {ordem_i.id} (pos {i}) com {ordem_j.id} (pos {j}).")
                    print(f"    Nova Penalidade: {nova_solucao.penalidade_total}")

                    melhor_solucao = nova_solucao
                    melhor_penalidade = nova_solucao.penalidade_total
                    melhor_N = vizinho_N

                    melhorou = True
                    break

        iteracao += 1
        if not melhorou and (time.time() - inicio_execucao) < max_tempo_segundos:
            print(
                f"  Resumo Iteração {iteracao}: {trocas_avaliadas} pares vistos (Foco), {trocas_efetivas} calculados.")

    tempo_total = time.time() - inicio_execucao
    print(f"--- Fim Busca Local. Tempo: {tempo_total:.2f}s. Penalidade Final: {melhor_penalidade} ---\n")

    melhor_solucao.N = melhor_N
    return melhor_solucao