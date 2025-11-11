from typing import List, Tuple, Dict
from collections import defaultdict
from src.modelo import Equipe, OrdemManutencao, Alocacao, Solucao


def calcular_ocupacao(ordens: List[OrdemManutencao], equipes: List[Equipe]) -> Dict[str, float]:
    duracao_total = defaultdict(int)
    qtd_equipes = defaultdict(int)

    for o in ordens:
        duracao_total[o.especialidade.lower()] += o.duracao
    for e in equipes:
        qtd_equipes[e.especialidade.lower()] += 1

    ocupacao = {}
    for especialidade in duracao_total:
        if qtd_equipes[especialidade] > 0:
            ocupacao[especialidade] = duracao_total[especialidade] / qtd_equipes[especialidade]
        else:
            ocupacao[especialidade] = 0.0
    return ocupacao


def organizar_equipes_por_ocupacao(equipes: List[Equipe], ocupacao: Dict[str, float]) -> List[Equipe]:
    equipes_restantes = equipes.copy()
    equipes_ordenadas = []

    while equipes_restantes:
        melhor_eq = None
        maior_ocupacao = -1.0
        for e in equipes_restantes:
            esp = e.especialidade.lower()
            if ocupacao.get(esp, 0.0) > maior_ocupacao:
                maior_ocupacao = ocupacao.get(esp, 0.0)
                melhor_eq = e
        equipes_ordenadas.append(melhor_eq)
        equipes_restantes.remove(melhor_eq)
    return equipes_ordenadas


def alocar_ordens(ordens: List[OrdemManutencao], equipes: List[Equipe], N: List[OrdemManutencao]) \
        -> Tuple[Solucao, int]:
    solucao = Solucao()
    alocadas = []

    ocupacao = calcular_ocupacao(ordens, equipes)
    equipes_ordenadas = organizar_equipes_por_ocupacao(equipes, ocupacao)

    for equipe in equipes_ordenadas:
        hk = equipe.disponibilidade
        C = [c for c in N if c.especialidade.lower() == equipe.especialidade.lower() and c not in alocadas]

        while C:
            c = C[0]
            C = C[1:]

            inicioc = c.inicio
            fimc = inicioc + c.duracao

            conflito = True
            while conflito and fimc <= c.fim and fimc <= hk:
                conflito = False
                for s in solucao.ordens_alocadas:
                    # conflito mesma equipe
                    if s.equipe.id == equipe.id and not (fimc <= s.inicio_execucao or inicioc >= s.fim_execucao):
                        inicioc = s.fim_execucao
                        fimc = inicioc + c.duracao
                        conflito = True
                        break

                    # conflito mesma ferramenta
                    if s.ordem.equipamento == c.equipamento and not (
                            fimc <= s.inicio_execucao or inicioc >= s.fim_execucao):
                        inicioc = s.fim_execucao
                        fimc = inicioc + c.duracao
                        conflito = True
                        break

            if fimc > c.fim or fimc > hk:
                continue

            alocacao = Alocacao(ordem=c, equipe=equipe, inicio_execucao=inicioc, fim_execucao=fimc)
            solucao.ordens_alocadas.append(alocacao)
            alocadas.append(c)

    nao_alocadas = [o for o in ordens if o not in alocadas]
    penalidade_total = sum(o.penalidade for o in nao_alocadas)
    solucao.custo_total = penalidade_total
    solucao.ordens_nao_alocadas = nao_alocadas
    return solucao, penalidade_total
