import csv
import random

nome_arquivo = "ordens.csv"

especialidades = ["Elétrica", "Mecânica"]
equipamentos = ["Caminhão", "Carro", "Moto"]
tarefas = ["Alinhamento", "Revisão de motor", "Revisão elétrica"]

num_ordens = 100
periodos = 20
max_duracao = 4
max_penalidade = 100

with open(nome_arquivo, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "tarefa", "equipamento", "especialidade", "inicio", "fim", "duracao", "penalidade"])
    for i in range(1, num_ordens + 1):
        especialidade = random.choice(especialidades)
        duracao = random.randint(1, max_duracao)
        inicio = random.randint(0, periodos - duracao)
        fim = inicio + duracao
        penalidade = random.randint(10, max_penalidade)
        writer.writerow([
            i,
            random.choice(tarefas),
            random.choice(equipamentos),
            especialidade,
            inicio,
            fim,
            duracao,
            penalidade
        ])
print(f"{nome_arquivo} gerado com sucesso.")
