from src.modelo import Solucao
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import hashlib


def gerar_cores_equipamentos(solucao: Solucao):
    equipamentos = {aloc.ordem.equipamento for aloc in solucao.ordens_alocadas}
    cmap = cm.get_cmap('prism')
    cores_equipamentos = {}
    for eq in equipamentos:
        h = int(hashlib.sha256(eq.encode()).hexdigest(), 16)
        indice = (h % 1000) / 1000.0
        cor = cmap(indice)
        cores_equipamentos[eq] = mcolors.rgb2hex(cor)
    return cores_equipamentos


def plotar_grafico_gantt(solucao: Solucao):
    equipes = sorted({aloc.equipe.nome for aloc in solucao.ordens_alocadas})
    equipes.reverse()

    altura_barra = 0.5
    espacamento = 0.8
    altura_por_equipe = 0.6
    margem_superior_inferior = 1
    largura_figura = 10
    altura_figura = len(equipes) * altura_por_equipe + margem_superior_inferior

    fig, ax = plt.subplots(figsize=(largura_figura, altura_figura))
    cores_equipamentos = gerar_cores_equipamentos(solucao)

    for aloc in solucao.ordens_alocadas:
        y = equipes.index(aloc.equipe.nome)
        x_inicio = aloc.inicio_execucao
        duracao = aloc.fim_execucao - aloc.inicio_execucao
        cor = cores_equipamentos.get(aloc.ordem.equipamento, "#7f8c8d")

        ax.broken_barh([(x_inicio, duracao)],
                       (y * espacamento - altura_barra / 2, altura_barra),
                       facecolors=cor, edgecolor='black', linewidth=0.8)

        ax.text(x_inicio + duracao / 2, y * espacamento,
                str(aloc.ordem.id), ha='center', va='center',
                color='black', fontsize=9, weight='bold')

    ax.set_yticks([y * espacamento for y in range(len(equipes))])
    ax.set_yticklabels(equipes)
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position('top')
    ax.set_xlabel('Período')

    ax.set_ylim(-0.5, (len(equipes) - 1) * espacamento + 0.5)
    ax.set_aspect('auto')
    ax.grid(True, axis='x', linestyle='--', alpha=0.4)

    legendas = [
        mpatches.Patch(color=cor, label=equip)
        for equip, cor in sorted(cores_equipamentos.items())
    ]
    ax.legend(handles=legendas, title="Equipamento",
              bbox_to_anchor=(1.02, 1), loc='upper left',
              borderaxespad=0., edgecolor='black')

    ax.text(0, -0.15,
            f"N = {solucao.N_ids}\nNão alocadas = {solucao.ordens_nao_alocadas_ids}\n"
            f"Penalidade total = {solucao.penalidade_total}", transform=ax.transAxes, fontsize=9,
            color="black", ha="left", va="top", linespacing=1.4)

    plt.savefig("grafico_gantt.png", dpi=900, bbox_inches="tight")
    print("Gráfico salvo em grafico_gantt.png")
