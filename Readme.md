# Detector de Outliers

Um programa simples para analisar conjuntos de dados e identificar valores atípicos (outliers) usando o método z-score.

## Funcionalidades

- Inserção de conjuntos numéricos para análise
- Cálculo de estatísticas básicas (média, desvio padrão, valores mínimo e máximo)
- Detecção automática de outliers usando z-score
- Ajuste de sensibilidade para detecção de outliers
- Interface de console amigável

## Como usar

1. Execute o arquivo `main.py` ou o executável gerado
2. Insira a quantidade de números que deseja analisar
3. Digite cada número do conjunto
4. Analise os resultados estatísticos e outliers detectados
5. Escolha entre analisar novo conjunto, modificar o conjunto atual, alterar sensibilidade ou sair

## Requisitos

- Python 3.6 ou superior (para executar o código fonte)
- Não são necessárias bibliotecas externas, apenas as bibliotecas padrão do Python

### Usando o executável

1. Baixe o arquivo executável da página de [Releases](https://github.com/Funkmnk/detector-de-outliers/releases)
2. Execute o arquivo `Detector_de_Outliers.exe`

### A partir do código fonte

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/detector-de-outliers.git

# Entre na pasta do projeto
cd detector-de-outliers

# Execute o programa
python main.py
```

## Estrutura do projeto

- `main.py`: Arquivo principal e ponto de entrada do programa
- `modulos/interface.py`: Funções de interface com o usuário
- `modulos/estatisticas.py`: Funções para cálculos estatísticos

## Como funciona a detecção de outliers

Este programa utiliza o método estatístico z-score para identificar valores atípicos (outliers) em conjuntos de dados:

1. Calcula a média e o desvio padrão do conjunto
2. Para cada valor, calcula seu z-score: (valor - média) / desvio_padrão
3. Um valor é considerado outlier se seu z-score absoluto for maior que a sensibilidade definida (padrão: 2.0)
