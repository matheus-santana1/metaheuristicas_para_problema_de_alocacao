from typing import List


class OrdemManutencao:
    def __init__(self, id: int, tarefa: str, equipamento: str, especialidade: str, inicio: int, fim: int,
                 duracao: int, penalidade: int):
        self.id = id
        self.tarefa = tarefa
        self.equipamento = equipamento
        self.especialidade = especialidade
        self.inicio = inicio
        self.fim = fim
        self.duracao = duracao
        self.penalidade = penalidade

    def __repr__(self):
        return (f"Ordem(id={self.id}, tarefa={self.tarefa}, especialidade={self.especialidade}, "
                f"janela_de_trabalho=[{self.inicio}, {self.fim}], duracao={self.duracao}, penalidade={self.penalidade})")

    def __str__(self):
        return f"({self.id}) Tarefa: {self.tarefa} {self.equipamento} {self.especialidade.upper()}"


class Equipe:
    def __init__(self, id: int, nome: str, especialidade: str, disponibilidade: int):
        self.id = id
        self.nome = nome
        self.especialidade = especialidade
        self.disponibilidade = disponibilidade

    def __repr__(self):
        return (f"Equipe(id={self.id}, nome={self.nome}, especialidade={self.especialidade}, "
                f"disponibilidade={self.disponibilidade})")


class Alocacao:
    """
    Classe auxiliar para a Solucao.
    Registra uma ordem que FOI alocada, em qual equipe e em qual horário.
    Isto representa um item no gráfico de Gantt (Figura 2).
    """

    def __init__(self, ordem: OrdemManutencao, equipe: Equipe,
                 inicio_execucao: int, fim_execucao: int):
        self.ordem = ordem
        self.equipe = equipe
        self.inicio_execucao = inicio_execucao
        self.fim_execucao = fim_execucao

    def __repr__(self):
        return (f"[equipe {self.equipe.id}: ordem {self.ordem.id} "
                f"executando em [{self.inicio_execucao}, {self.fim_execucao}]]")


class Solucao:
    def __init__(self):
        self.penalidade_total: int = 0
        self.ordens_alocadas: List[Alocacao] = []
        self.ordens_nao_alocadas: List[OrdemManutencao] = []
        self.N: List[OrdemManutencao] = []

    def __repr__(self):
        return (f"solucao("
                f"penalidade_total={self.penalidade_total}, "
                f"alocadas={len(self.ordens_alocadas)}, "
                f"nao_alocadas={len(self.ordens_nao_alocadas)}, "
                f"N={self.N_ids})")

    @property
    def N_ids(self):
        return [n.id for n in self.N]

    @property
    def ordens_nao_alocadas_ids(self):
        return [ordem.id for ordem in self.ordens_nao_alocadas]
