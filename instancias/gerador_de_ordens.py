import csv
import random

nome_arquivo_ordens = "ordens.csv"
nome_arquivo_equipes = "equipes.csv"

especialidades = ["Elétrica", "Mecânica"]
equipamentos = [
    "Caminhão", "Carro", "Moto", "Trator", "Retroescavadeira",
    "Empilhadeira", "Guindaste", "Betoneira", "Pá Carregadeira",
    "Rolo Compressor", "Furgão", "Van", "Ônibus", "Bicicleta",
    "Helicóptero", "Avião", "Barco", "Jet Ski", "Quadriciclo"
]
num_equipamentos = 19
tarefas = ["Alinhamento", "Revisão de motor", "Revisão elétrica"]

num_ordens = 5000
periodos = 8000
max_duracao = 4
max_penalidade = 100

num_equipes_eletrica = 10
num_equipes_mecanica = 10
disponibilidade_padrao = periodos

with open(nome_arquivo_equipes, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "nome", "especialidade", "disponibilidade"])
    id_atual = 1
    for i in range(num_equipes_eletrica):
        letra = chr(65 + i)
        writer.writerow([id_atual, f"Elétrica {letra}", "Elétrica", disponibilidade_padrao])
        id_atual += 1
    for i in range(num_equipes_mecanica):
        letra = chr(65 + i)
        writer.writerow([id_atual, f"Mecânica {letra}", "Mecânica", disponibilidade_padrao])
        id_atual += 1
print(f"{nome_arquivo_equipes} gerado com sucesso.")

with open(nome_arquivo_ordens, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "tarefa", "equipamento", "especialidade", "inicio", "fim", "duracao", "penalidade"])
    equipamentos = random.sample(equipamentos, k=num_equipamentos)
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
print(f"{nome_arquivo_ordens} gerado com sucesso.")
