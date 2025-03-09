'''
As chamadas de interface ficaram aqui
'''

# Importando módulos de cálculo
from modulos.estatisticas import (
    calculo_media,
    calculo_desvio_padrao,
    calculo_minimo_e_maximo,
    calculo_de_outliers,
    calculo_porcentagem_conjunto
)


def apresentacao():
    '''
    Exibe a tela de apresentação inicial do programa.
    
    Limpa a tela e mostra o título, versão e uma breve descrição
    do programa de detecção de outliers.
    
    Returns:
        None
    '''
    
    limpar_tela()
    print("=== DETECTOR DE OUTLIERS - VERSÃO 1.0 ===")
    print()
    print("Bem-vindo ao sistema de detecção de Outliers!")
    print("Este programa analisa um conjunto de dados e encontra valores atípicos.")
    print()


def obter_quantidade_de_analise():
    '''
    Solicita ao usuário a quantidade de números para análise.
    
    Continua solicitando ao usuário até receber um número inteiro
    positivo válido.
    
    Returns:
        int: Quantidade de números a serem analisados
    
    Raises:
        ValueError: Tratado internamente quando o usuário insere 
                    um valor não numérico
    '''
    
    while True:
        try:
            qtdanalise = int(input("Quantos números você deseja analisar?: "))
            
            # Verificação adicional para valores não positivos
            if qtdanalise <= 0:
                print("A quantidade deve ser maior que zero. Tente novamente.")
                continue
                
            print()
            
            # Retorna apenas se o valor for válido
            return qtdanalise
            
        except ValueError:
            print("Por favor, digite um número inteiro válido.")


def leitura_dos_dados(qtdanalise):
    '''
    Solicita ao usuário a entrada de cada número do conjunto de dados.
    
    Args:
        qtdanalise (int): Quantidade de números a serem inseridos
    
    Returns:
        list: Lista com os valores numéricos inseridos pelo usuário
    
    Raises:
        ValueError: Tratado internamente quando o usuário insere 
                    um valor não numérico
    '''
    
    # Definição da lista
    vetor_analise = []
    
    for i in range(0, qtdanalise):
        while True:
            try:
                valor = float(input(f"Digite o {i + 1}° número: "))
                vetor_analise.append(valor)
                break
                
            except ValueError:
                print("Por favor, digite um número válido.")
    
    return vetor_analise


def apresentacao_dos_dados(vetor_analise, qtdanalise):
    '''
    Exibe os dados inseridos pelo usuário em formato de lista.
    
    Args:
        vetor_analise (list): Lista com os valores numéricos inseridos
        qtdanalise (int): Quantidade de números inseridos
    
    Returns:
        None
    '''
    
    # Apresenta os valores inseridos
    print()
    print("Conjunto de dados inseridos: [", end="")
    for i in range (0, qtdanalise):
        print(f"{vetor_analise[i]}", end="")
        if i < qtdanalise - 1:
            print(", ", end="")
    print("]", end="")


def confirmacao_dos_dados(qtdanalise, vetor_analise):
    '''
    Pergunta ao usuário se deseja corrigir algum dos dados inseridos.
    
    Se o usuário optar por corrigir, chama a função de leitura dos dados
    novamente e apresenta os novos dados.
    
    Args:
        qtdanalise (int): Quantidade de números inseridos
        vetor_analise (list): Lista com os valores numéricos inseridos
    
    Returns:
        list: Lista atualizada (ou não) com os valores numéricos
    '''
    
    print()
    while True:
        corrigir = input("Deseja corrigir algum número? (S/N): ")
        if corrigir.upper() in ["S", "N"]:
            break
        print("Por favor, digite apenas S ou N.")
    
    if corrigir.upper() == "S":
        print()
        vetor_analise = leitura_dos_dados(qtdanalise)
        apresentacao_dos_dados(vetor_analise, qtdanalise = qtdanalise)
        
    # Retornando a lista atualizada
    return vetor_analise


def apresentacao_analise_estatistica(media, desvio_padrao, menor, maior, qtdanalise):
    '''
    Exibe os resultados da análise estatística básica do conjunto de dados.
    
    Limpa a tela e mostra as estatísticas calculadas: média, desvio padrão,
    valor mínimo, valor máximo e total de elementos no conjunto.
    
    Args:
        media (float): Média do conjunto de dados
        desvio_padrao (float): Desvio padrão do conjunto de dados
        menor (float): Menor valor no conjunto de dados
        maior (float): Maior valor no conjunto de dados
        qtdanalise (int): Quantidade total de elementos no conjunto
    
    Returns:
        None
    '''
    limpar_tela()
    print("----- ANÁLISE ESTATÍSTICA -----")
    print()
    print("Calculando estatísticas básicas...")
    print()
    print(f"Média: {media:.2f}")
    print(f"Desvio Padrão: {desvio_padrao:.2f}")
    print(f"Valor Mínimo: {menor}")
    print(f"Valor Máximo: {maior}")
    print(f"Total de Elementos: {qtdanalise}")
    print()
    input("Pressione ENTER para continuar...")


def apresentacao_deteccao_de_outliers():
    '''
    Exibe o cabeçalho da seção de detecção de outliers.
    
    Limpa a tela e apresenta o título da seção de detecção de outliers.
    
    Returns:
        None
    '''
    
    limpar_tela()
    print("----- DETECÇÃO DE OUTLIERS -----")
    print()


def obter_sensibilidade():
    '''
    Obtém ou permite ao usuário alterar a sensibilidade da detecção de outliers.
    
    A sensibilidade determina quantos desvios padrões um valor precisa estar
    da média para ser considerado um outlier. O valor padrão é 2.0, mas o
    usuário pode alterá-lo.
    
    Returns:
        float: Valor de sensibilidade para detecção de outliers
    '''
    
    # Sensibilidade padrão
    sensibilidade = 2.0
    
    # Confirmação de sensibilidade
    print(f"Sensibilidade atual: {sensibilidade:.1f} (valores com z-score > que {sensibilidade:.1f} são considerados outliers)")
    corrigir_sensibilidade = input("Deseja alterar a sensibilidade atual? (S/N): ")
    
    # Função de correção
    def correcao_sensibilidade(sensibilidade):
            print()
            sensibilidade = float(input(f"Digite a nova sensibilidade (atual: {sensibilidade:.2f}): "))
            return sensibilidade
    
    match corrigir_sensibilidade:
        case "S" | "s":
              sensibilidade = correcao_sensibilidade(sensibilidade)
              print()
              print(f"Sensibilidade atualizada para {sensibilidade:.1f}")
    
    # Retornando a sensibilidade escolhida
    return sensibilidade


def apresentacao_analise_final(vetor_analise, vetor_outliers, vetor_z_score, qtdoutliers, qtdanalise, pctconjunto, sensibilidade, total_conjuntos, total_outliers, total_elementos):
    '''
    Apresenta o resultado final da análise de outliers.
    
    Exibe informações detalhadas sobre os outliers encontrados, 
    incluindo seus valores, z-scores e uma interpretação dos resultados.
    
    Args:
        vetor_analise (list): Lista com os valores numéricos analisados
        vetor_outliers (list): Lista de tuplas (índice, valor, z-score) dos outliers
        vetor_z_score (list): Lista com os z-scores calculados para cada valor
        qtdoutliers (int): Quantidade de outliers detectados
        qtdanalise (int): Quantidade total de elementos analisados
        pctconjunto (float): Percentual de outliers em relação ao conjunto
        sensibilidade (float): Valor de sensibilidade utilizado na detecção
        total_conjuntos (int): Número total de conjuntos analisados na sessão
        total_outliers (int): Número total de outliers detectados na sessão
        total_elementos (int): Número total de elementos analisados na sessão
    
    Returns:
        tuple: (total_conjuntos, total_outliers, total_elementos) atualizados
    '''
    
    limpar_tela()
    print("----- DETECÇÃO DE OUTLIERS -----")
    print()
    print("Analisando dados...")
    print()
    print("RESULTADO DA ANÁLISE:")
    print()
    print(f"✓ Total de números analisados: {qtdanalise}")
    print(f"✓ Outliers encontrados: {qtdoutliers}", end="")
    if qtdoutliers > 0:
        print(f" ({pctconjunto:.1f}% do conjunto)")
    print()
    
    if qtdoutliers > 0:
        print("LISTA DE OUTLIERS:")
        for idx, valor, z_score in vetor_outliers:
            direcao = "acima" if z_score > 0 else "abaixo"
            print(f"→ {valor}: z-score = {abs(z_score):.2f} ", end="")
            print("(Alto)" if z_score > 0 else "(Baixo)")
            print(f"    Esse valor está {abs(z_score):.2f} desvios padrão {direcao} da média")
    print()
    
    print("INTERPRETAÇÃO:")
    if qtdoutliers == 0:
        print("O conjunto de dados apresenta excelente consistência, sem valores atípicos.")
    # Acessa o primeiro (e único) outlier da lista
    elif qtdoutliers == 1:
        # Acessa o valor (segundo elemento da tupla)
        outlier_valor = vetor_outliers[0][1]
        # Acessa o z-score (terceiro elemento da tupla)
        z_score = vetor_outliers[0][2]
        direcao = "alto" if z_score > 0 else "baixo"
        print("O conjunto de dados apresenta boa consistência, com apenas um valor atípico.")
        print(f"O outlier identificado ({outlier_valor}) é significativamente mais {direcao} que os demais valores.")
    elif qtdoutliers <= qtdanalise * 0.10:
        print("O conjunto de dados apresenta consistência razoável, com poucos valores atípicos.")
    else:
        print("O conjunto de dados apresenta baixa consistência, com muitos valores atípicos.")
        print("Recomenda-se revisar a coleta de dados ou ajustar a sensibilidade da análise.")
    print()
    input("Pressione ENTER para continuar...")
    limpar_tela()
    
    # Variável de controle para a apresentação final
    total_outliers = total_outliers + qtdoutliers
    
    # Retornando as informações de controle para apresentação final
    return total_conjuntos, total_outliers, total_elementos


def menu_escolha():
    '''
    Exibe o menu de opções e obtém a escolha do usuário.
    
    Limpa a tela, apresenta as opções disponíveis e valida a entrada do usuário
    até receber uma opção válida.
    
    Returns:
        str: Opção escolhida pelo usuário ('1', '2', '3' ou '4')
    '''
    
    limpar_tela()
    print("----- OPÇÕES -----")
    print("O que você deseja fazer agora?")
    print()
    print("1. Analisar novo conjunto de dados")
    print("2. Modificar o conjunto atual")
    print("3. Alterar sensibilidade da detecção")
    print("4. Sair do programa")
    print()
    
    while True:
        opcao_menu = input("Digite sua opção: ")
        if opcao_menu in ["1", "2", "3", "4"]:
            return opcao_menu
        print("Opção inválida! Por favor, digite 1, 2, 3 ou 4.")


def escolha_do_menu(opcao_menu,total_conjuntos, total_outliers, total_elementos, sensibilidade, vetor_analise, qtdanalise) :
    '''
    Processa a escolha do usuário no menu principal.
    
    Realiza a ação correspondente à opção selecionada pelo usuário:
    1. Analisar novo conjunto de dados
    2. Modificar o conjunto atual
    3. Alterar sensibilidade da detecção
    4. Sair do programa
    
    Args:
        opcao_menu (str): Opção escolhida pelo usuário
        total_conjuntos (int): Número total de conjuntos analisados na sessão
        total_outliers (int): Número total de outliers detectados na sessão
        total_elementos (int): Número total de elementos analisados na sessão
        sensibilidade (float): Valor de sensibilidade utilizado na detecção
        vetor_analise (list): Lista com os valores numéricos atuais
        qtdanalise (int): Quantidade de elementos no conjunto atual
    
    Returns:
        tuple or str: Retorna uma tupla (total_conjuntos, total_outliers, total_elementos, sensibilidade)
                      ou a opção do menu (no caso da opção 4)
    '''
    
    limpar_tela()
    match opcao_menu:
        case "1":
            print()
            print("----- NOVO CONJUNTO DE DADOS -----")
            print()
            # Obtendo quantidade da nova leitura
            qtdanalise = obter_quantidade_de_analise()
            print()
            
            # Lendo os novos dados
            vetor_analise = leitura_dos_dados(qtdanalise)
            
            # Apresentando os valores lidos
            apresentacao_dos_dados(vetor_analise, qtdanalise = qtdanalise)
            
            # Confirmando os valores lidos
            vetor_analise = confirmacao_dos_dados(qtdanalise, vetor_analise)
            
            # Incremento do contador de conjuntos e elementos
            total_conjuntos += 1
            total_elementos += qtdanalise
            
            # Análise dos dados
            total_conjuntos, total_outliers, total_elementos, sensibilidade = analisar_dados(vetor_analise, qtdanalise, None, total_conjuntos, total_outliers, total_elementos)
            
            # Retornando os dados
            return total_conjuntos, total_outliers, total_elementos, sensibilidade

        case "2":
            print()
            # Corrigindo e apresentando os dados
            vetor_analise = leitura_dos_dados(qtdanalise)
            apresentacao_dos_dados(vetor_analise, qtdanalise = qtdanalise)
            
            # Incremento do contador de conjuntos e elementos
            total_conjuntos += 1
            total_elementos += qtdanalise
            
            # Análise dos dados
            total_conjuntos, total_outliers, total_elementos, sensibilidade = analisar_dados(vetor_analise, qtdanalise, None, total_conjuntos, total_outliers, total_elementos)
            
            # Retornando os dados
            return total_conjuntos, total_outliers, total_elementos, sensibilidade

        case "3":
            print()
            sensibilidade = float(input(f"Digite a nova sensibilidade (atual: {sensibilidade:.2f}): "))
            print()
            print(f"Sensibilidade atualizada para {sensibilidade:.1f}")
            print()
            print("Recalculando outliers...")
            print()
            
            # Análise dos dados
            total_conjuntos, total_outliers, total_elementos, sensibilidade = analisar_dados(vetor_analise, qtdanalise, sensibilidade, total_conjuntos, total_outliers, total_elementos)
            
            # Retorna os valores atualizados
            return total_conjuntos, total_outliers, total_elementos, sensibilidade
        case "4":
            # Altera a variável para sair do menu
            opcao_menu = 4
            # Retornando a escolha
            return opcao_menu
        case _:
            print("Opção inválida!")
            # Retornando os dados
            return total_conjuntos, total_outliers, total_elementos, sensibilidade


def analisar_dados(vetor_analise, qtdanalise, sensibilidade=None, total_conjuntos=0, total_outliers=0, total_elementos=0):
    '''
    Realiza a análise completa de um conjunto de dados.
    
    Calcula estatísticas básicas (média, desvio padrão, mínimo e máximo),
    detecta outliers conforme a sensibilidade especificada e apresenta
    os resultados.
    
    Args:
        vetor_analise (list): Lista com os valores numéricos a serem analisados
        qtdanalise (int): Quantidade de elementos no conjunto
        sensibilidade (float, optional): Valor de sensibilidade para detecção de outliers.
                                         Se None, será solicitado ao usuário.
        total_conjuntos (int, optional): Contador de conjuntos analisados. Padrão é 0.
        total_outliers (int, optional): Contador de outliers detectados. Padrão é 0.
        total_elementos (int, optional): Contador de elementos analisados. Padrão é 0.
    
    Returns:
        tuple: (total_conjuntos, total_outliers, total_elementos, sensibilidade)
    '''
    
    # Calculando a média
    media = calculo_media(vetor_analise, qtdanalise)
    
    # Calculando o desvio padrão
    desvio_padrao = calculo_desvio_padrao(vetor_analise, qtdanalise, media=media)
    
    # Calculando o menor e maior números do conjunto
    maior = calculo_minimo_e_maximo(vetor_analise, qtdanalise)[0]
    menor = calculo_minimo_e_maximo(vetor_analise, qtdanalise)[1]
    
    # Análise estatística
    apresentacao_analise_estatistica(media, desvio_padrao, menor, maior, qtdanalise)
    
    # Apresentação das informações de Outliers
    apresentacao_deteccao_de_outliers()
    
    # Sensibilidade de detecção (se não fornecida)
    if sensibilidade is None:
        sensibilidade = obter_sensibilidade()
    
    # Calculanda os outliers
    qtdoutliers, vetor_outliers, vetor_z_score = calculo_de_outliers(qtdanalise, vetor_analise, media, desvio_padrao, sensibilidade)
    
    # Calculanda a porcentagem do conjunto
    pctconjunto = calculo_porcentagem_conjunto(qtdoutliers, qtdanalise)
    
    # Apresentação do resultado final
    total_conjuntos, total_outliers, total_elementos = apresentacao_analise_final(vetor_analise, vetor_outliers, vetor_z_score, qtdoutliers, qtdanalise, pctconjunto, sensibilidade, total_conjuntos, total_outliers, total_elementos)
    
    # Retornando os dados
    return total_conjuntos, total_outliers, total_elementos, sensibilidade


def limpar_tela():
    '''
    Limpa a tela do console.
    
    Utiliza comandos específicos do sistema operacional para limpar
    a tela do console (cls no Windows, clear em sistemas Unix).
    
    Returns:
        None
    '''
    
    import os
    os.system('cls' if os.name == 'nt' else 'clear')