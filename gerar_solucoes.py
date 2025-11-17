import subprocess

tipos = ["simples", "parcialmente_gulosa"]

for caso in range(1, 3 + 1):
    for tipo in tipos:
        cmd = [
            "python", "main.py",
            f"--equipes=instancias/caso_{caso}/equipes.csv",
            f"--ordem=instancias/caso_{caso}/ordens.csv",
            "--seed=10",
            f"--arquivo=caso_{caso}",
            f"--tipo_heuristica={tipo}"
        ]
        print("Executando:", " ".join(cmd))
        subprocess.run(cmd)
