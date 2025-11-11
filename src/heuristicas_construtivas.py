from collections import Counter
from typing import List
from src.modelo import OrdemManutencao


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


def heuristica_por_ferramenta(ordens: List[OrdemManutencao]) -> List[OrdemManutencao]:
    N = []
    contagem = Counter(o.equipamento for o in ordens)
    equipamentos = list(contagem.keys())
    usados = set()
    while len(usados) < len(equipamentos):
        mais_usado = None
        maior_freq = -1
        for eq in equipamentos:
            if eq not in usados and contagem[eq] > maior_freq:
                mais_usado = eq
                maior_freq = contagem[eq]
        usados.add(mais_usado)

        C = [o for o in ordens if o.equipamento == mais_usado]
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
