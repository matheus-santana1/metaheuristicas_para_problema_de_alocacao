import csv
import random

num_ordens = 1000
periodos = 52
especialidades = ["Mecânica", "Elétrica"]
max_duracao = 5
max_penalidade = 100
nome_arquivo = "ordem_2.csv"

with open("ordem_3.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "tarefa", "equipamento", "especialidade", "inicio", "fim", "duracao", "penalidade"])
    for i in range(1, num_ordens + 1):
        especialidade = random.choice(especialidades)
        inicio = random.randint(0, periodos - 1)
        duracao = random.randint(1, max_duracao)
        fim = min(inicio + duracao + random.randint(1, 10), periodos)
        penalidade = random.randint(10, max_penalidade)
        writer.writerow(
            [i, f"Tarefa {i}", f"Equipamento {chr(65 + (i % 26))}", especialidade, inicio, fim, duracao, penalidade]
        )
print(f"{nome_arquivo} gerado com sucesso.")
