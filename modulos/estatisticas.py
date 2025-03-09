'''
Todos os cálculos estatísticos vão ficar aqui.
'''

# Importanto biblioteca
import math

def calculo_media(vetor_analise, qtdanalise):
    '''
    Calcula a média aritmética de um conjunto de dados.
    
    Args:
        vetor_analise (list): Lista de valores numéricos
        qtdanalise (int): Quantidade de elementos na lista
    
    Returns:
        float: Média aritmética do conjunto de dados
    
    Examples:
        >>> calculo_media([10, 20, 30, 40, 50], 5)
        30.0
    '''
    
    soma = sum(vetor_analise)
    media = soma / qtdanalise
    return media


def calculo_desvio_padrao(vetor_analise, qtdanalise, media):
    '''
    Calcula o desvio padrão de um conjunto de dados.
    
    O desvio padrão é uma medida de dispersão que indica quão distantes
    os valores estão da média do conjunto. O cálculo segue os seguintes passos:
    1. Calcula a diferença entre cada valor e a média
    2. Eleva cada diferença ao quadrado
    3. Soma todas as diferenças ao quadrado
    4. Divide pelo número de elementos
    5. Calcula a raiz quadrada do resultado
    
    Args:
        vetor_analise (list): Lista de valores numéricos
        qtdanalise (int): Quantidade de elementos na lista
        media (float): Média aritmética do conjunto de dados
    
    Returns:
        float: Desvio padrão do conjunto de dados
    
    Examples:
        >>> calculo_desvio_padrao([10, 20, 30, 40, 50], 5, 30.0)
        14.14
    '''
    
    # 1. Calculando a diferença entre cada valor e a média
    vetor_desvio_diferenca: list[float] = [0 for x in range(qtdanalise)]
    for i in range (0, qtdanalise):
        vetor_desvio_diferenca[i] = vetor_analise[i] - media
    
    # 2. Elevando as diferenças ao quadrado e somando
    soma_diferenca = 0
    for i in range (0, qtdanalise):
        soma_diferenca = soma_diferenca + (vetor_desvio_diferenca[i] * vetor_desvio_diferenca[i])
    
    # 3. Dividindo pelo número de elemtos do conjunto
    conjunto = soma_diferenca / qtdanalise
    
    # 4. Tirando a raiz do conjunto
    desvio_padrao = math.sqrt(conjunto)
    
    # Retornando o desvio padrão
    return desvio_padrao


def calculo_minimo_e_maximo(vetor_analise, qtdanalise):
    '''
    Encontra os valores mínimo e máximo em um conjunto de dados.
    
    Args:
        vetor_analise (list): Lista de valores numéricos
        qtdanalise (int): Quantidade de elementos na lista
    
    Returns:
        tuple: (maior, menor) contendo o valor máximo e mínimo do conjunto
    
    Examples:
        >>> calculo_minimo_e_maximo([10, 20, 30, 40, 50], 5)
        (50, 10)
    '''
    
    menor = vetor_analise[0]
    maior = vetor_analise[0]
    for i in range (0, qtdanalise):
        # Menor
        if vetor_analise[i] < menor:
            menor = vetor_analise[i]
        # Maior
        if vetor_analise[i] > maior:
            maior = vetor_analise[i]

    # Retorna os valores
    return maior, menor


def calculo_de_outliers(qtdanalise, vetor_analise, media, desvio_padrao, sensibilidade):
    '''
    Identifica outliers em um conjunto de dados usando o método Z-score.
    
    Um valor é considerado outlier se seu Z-score (quantos desvios padrões
    está da média) for maior que o valor de sensibilidade.
    
    Args:
        qtdanalise (int): Quantidade de elementos na lista
        vetor_analise (list): Lista de valores numéricos
        media (float): Média aritmética do conjunto de dados
        desvio_padrao (float): Desvio padrão do conjunto de dados
        sensibilidade (float): Limiar de Z-score para identificar outliers
    
    Returns:
        tuple: (qtdoutliers, vetor_outliers, vetor_z_score)
               - qtdoutliers (int): Quantidade de outliers encontrados
               - vetor_outliers (list): Lista de tuplas (índice, valor, z-score) dos outliers
               - vetor_z_score (list): Lista com os z-scores calculados para cada valor
    
    Notes:
        - Se o desvio padrão for zero, retorna sem encontrar outliers
        - Um Z-score positivo indica valor acima da média
        - Um Z-score negativo indica valor abaixo da média
    '''
    
    # Verificação de segurança para evitar divisão por zero
    if desvio_padrao == 0:
        return 0, [], [0] * qtdanalise
    
    # Lista para armazenar os outliers
    vetor_outliers = []
    vetor_z_score = [0] * qtdanalise
    
    # Aplicando a fórmula de z-score na checagem
    qtdoutliers = 0
    for i in range(0, qtdanalise):
        try:
            vetor_z_score[i] = (vetor_analise[i] - media) / desvio_padrao
            # Detecta outliers em ambas as direções usando abs()
            if abs(vetor_z_score[i]) > sensibilidade:
                vetor_outliers.append((i, vetor_analise[i], vetor_z_score[i]))
                qtdoutliers += 1
                
        except ZeroDivisionError:
            # Caso ainda ocorra divisão por zero
            vetor_z_score[i] = 0
            
    # Retornando os cálculos
    return qtdoutliers, vetor_outliers, vetor_z_score


def calculo_porcentagem_conjunto(qtdoutliers, qtdanalise):
    '''
    Calcula a porcentagem de outliers em relação ao total de elementos.
    
    Args:
        qtdoutliers (int): Quantidade de outliers encontrados
        qtdanalise (int): Quantidade total de elementos analisados
    
    Returns:
        float: Percentual de outliers em relação ao conjunto (0-100)
    
    Examples:
        >>> calculo_porcentagem_conjunto(2, 100)
        2.0
    '''
    
    pctconjunto = (qtdoutliers / qtdanalise) * 100
    # Retornando o calculo
    return pctconjunto