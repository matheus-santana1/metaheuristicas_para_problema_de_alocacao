import subprocess

tipos = ["simples", "parcialmente_gulosa"]

for caso in range(1, 6 + 1):
    for tipo in tipos:
        cmd = [
            "python", "main.py",
            f"--equipes=instancias/caso_{caso}/equipes.csv",
            f"--ordem=instancias/caso_{caso}/ordens.csv",
            f"--seed=10",
            f"--tipo_movimento=swap",
            f"--max_tempo_segundos=100",
            f"--arquivo=caso_{caso}",
            f"--algoritmo={tipo}"
        ]
        print("Executando:", " ".join(cmd))
        subprocess.run(cmd)
