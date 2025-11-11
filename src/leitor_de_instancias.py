import csv
from typing import List
from src.modelo import Equipe, OrdemManutencao


def ler_equipes(caminho_arquivo: str) -> List[Equipe]:
    equipes = []
    with open(caminho_arquivo, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for linha in reader:
            equipe = Equipe(
                id=int(linha["id"]),
                nome=linha["nome"],
                especialidade=linha["especialidade"],
                disponibilidade=int(linha["disponibilidade"])
            )
            equipes.append(equipe)
    return equipes


def ler_ordens(caminho_arquivo: str) -> List[OrdemManutencao]:
    ordens = []
    with open(caminho_arquivo, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for linha in reader:
            ordem = OrdemManutencao(
                id=int(linha["id"]),
                tarefa=linha["tarefa"],
                equipamento=linha["equipamento"],
                especialidade=linha["especialidade"],
                inicio=int(linha["inicio"]),
                fim=int(linha["fim"]),
                duracao=int(linha["duracao"]),
                penalidade=int(linha["penalidade"])
            )
            ordens.append(ordem)
    return ordens
