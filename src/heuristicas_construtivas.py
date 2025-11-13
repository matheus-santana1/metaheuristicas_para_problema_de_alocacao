from typing import List
from src.modelo import OrdemManutencao
import random


def heuristica_simples(ordens: List[OrdemManutencao]) -> List[OrdemManutencao]:
    N = []
    C = ordens.copy()
    while C:
        melhor_ordem = None
        melhor_tempo = float('inf')
        melhor_penalidade = -1

        for c in C:
            if (c.fim < melhor_tempo) or (c.fim == melhor_tempo and c.penalidade > melhor_penalidade):
                melhor_ordem = c
                melhor_tempo = c.fim
                melhor_penalidade = c.penalidade
        N.append(melhor_ordem)
        C.remove(melhor_ordem)
    return N


def heuristica_parcialmente_gulosa(ordens: List[OrdemManutencao], alpha=0.5) -> List[OrdemManutencao]:
    """
    alpha: nível de aleatoriedade (0=guloso, 1=aleatório)
    """
    N = []
    C = ordens.copy()

    while C:
        prioridades = [o.penalidade / o.duracao for o in C]
        prioridade_max, prioridade_min = max(prioridades), min(prioridades)
        limiar = prioridade_max - alpha * (prioridade_max - prioridade_min)
        LRC = [o for o in C if o.penalidade / o.duracao >= limiar]
        escolhida = random.choice(LRC)
        N.append(escolhida)
        C.remove(escolhida)
    return N
