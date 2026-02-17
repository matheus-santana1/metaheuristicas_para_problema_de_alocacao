# Meta-heurísticas para o Problema de Sequenciamento de Ordens de Manutenção Preventiva de Longo Prazo

## 📜 Descrição do Projeto

Este repositório contém a implementação de **Heurísticas Construtivas**, **Busca Local** e a **Meta-heurística GRASP (Greedy Randomized Adaptive Search Procedure)** aplicadas ao **Problema de Sequenciamento de Ordens de Manutenção Preventiva de Longo Prazo (PPOMPLP)**.

O trabalho propõe e implementa abordagens heurísticas e meta-heurísticas para o PPOMPLP, que consiste em determinar a melhor sequência e alocação de atividades de manutenção entre as equipes disponíveis, ao longo de um horizonte de tempo predefinido. O objetivo é **reduzir o número de ordens não executadas** e **minimizar os custos relacionados à mão de obra e às penalidades** associadas a não execução das manutenções.

O modelo matemático e a metodologia são detalhados no artigo de referência:
> **Heurísticas Construtivas, de Busca Local e Meta-heurística GRASP Aplicadas Ao Problema de Sequenciamento de Ordens de Manutenção Preventiva de Longo Prazo**
> *Autores: Matheus Santana P. Costa, Rodrigo Max Tavares*

## 🛠️ Tecnologias Utilizadas

O projeto foi desenvolvido utilizando a linguagem de programação **Python**.

*   **Linguagem:** Python
*   **Dependências:** As dependências do projeto estão listadas no arquivo `requirements.txt`.

## 📂 Estrutura do Repositório

A estrutura de arquivos do projeto é organizada da seguinte forma:

```
.
├── imagens/                # Contém imagens e gráficos gerados pelo projeto (e.g., resultados, diagramas)
├── instancias/             # Conjunto de instâncias de teste para o problema de sequenciamento
│   └── caso_3/             # Exemplo de instância com arquivos equipes.csv e ordens.csv
├── src/                    # Código-fonte principal do projeto
│   ├── Solucao.py          # Classe que representa a solução do problema, contendo o vetor de sequenciamento (N) e a lista de alocações
│   ├── ...                 # Outros módulos e classes
├── args.py                 # Módulo para manipulação de argumentos de linha de comando
├── gerar_solucoes.py       # Script para gerar soluções de todos os casos de instâncias.
├── main.py                 # Ponto de entrada principal para a execução do projeto
└── requirements.txt        # Lista de dependências do Python
```

## 🚀 Como Executar o Projeto

### Pré-requisitos

Certifique-se de ter o **Python** instalado em sua máquina.

### 1. Clonar o Repositório

```bash
git clone https://github.com/matheus-santana1/metaheuristicas_para_problema_de_alocacao.git
cd metaheuristicas_para_problema_de_alocacao
```

### 2. Ambiente virtual (opcional)

```bash
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

### 3. Instalar as Dependências

Instale todas as bibliotecas necessárias utilizando o `pip`:

```bash
pip install -r requirements.txt
```

### 4. Executar o Algoritmo

Existem dois pontos de entrada principais, dependendo da fase de execução ou do algoritmo que você deseja rodar.

#### Execução Principal (via `main.py`)

O script `main.py` é o ponto de entrada principal para a execução das meta-heurísticas. Ele requer a especificação dos arquivos de instância e o tipo de heurística a ser utilizada.

**Exemplo de Execução:**

```bash
python main.py --equipes="instancias/caso_6/equipes.csv"
--ordem="instancias/caso_6/ordens.csv"
--arquivo="caso_6"
--algoritmo="parcialmente_gulosa"
--tipo_movimento="shift"
--seed=10
```

| Argumento          | Descrição                                                                    | Valores Possíveis (Exemplos)           |
|:-------------------|:-----------------------------------------------------------------------------|:---------------------------------------|
| `--equipes`        | Caminho para o arquivo CSV com os dados das equipes.                         | `instancias/caso_3/equipes.csv`        |
| `--ordem`          | Caminho para o arquivo CSV com os dados das ordens de manutenção.            | `instancias/caso_3/ordens.csv`         |
| `--seed`           | Semente para o gerador de números pseudoaleatórios (para reprodutibilidade). | `10`, `42`, etc.                       |
| `--arquivo`        | Nome base para os arquivos de saída (resultados).                            | `caso_3`                               |
| `--algoritmo`      | Tipo de heurística a ser executada.                                          | `simples`, `parcialmente_gulosa`, etc. |
| `--tipo_movimento` | Tipo de movimento a ser executado.                                           | `shift`, `swap`, etc.                  |

#### Execução de Geração de Soluções (via `gerar_solucoes.py`)

Este script pode ser usado para gerar soluções para todos os casos de instâncias.

**Exemplo de Execução:**

```bash
python gerar_solucoes.py
```

Consulte o arquivo `args.py` para a lista completa de opções e parâmetros disponíveis para ambos os scripts.

## ✅ Status do Projeto

- ![status](https://img.shields.io/badge/Heurísticas_Construtivas-OK-success)
- ![status](https://img.shields.io/badge/Busca_Local-OK-success)
- ![status](https://img.shields.io/badge/GRASP-Não_Implementado-critical)
- ![status](https://img.shields.io/badge/Testes_Instâncias-OK-success)
- ![status](https://img.shields.io/badge/Documentação_Completa-Não_Realizado-critical)

---

