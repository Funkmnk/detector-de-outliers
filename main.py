# Importando as funções
from modulos.interface import (
    apresentacao,
    obter_quantidade_de_analise,
    leitura_dos_dados,
    apresentacao_dos_dados,
    confirmacao_dos_dados,
    menu_escolha,
    escolha_do_menu,
    analisar_dados,
    limpar_tela
)

def main():
    '''
    Função principal que controla o fluxo do programa de detecção de outliers.
    
    Esta função inicializa o programa, gerencia variáveis de controle para
    estatísticas da sessão, obtém dados do usuário, realiza análises,
    exibe resultados e gerencia o menu de opções até que o usuário decida sair.
    
    Returns:
        None
    '''
    
    # Variáveis de controle para apresentação final
    total_conjuntos = 0
    total_outliers = 0
    total_elementos = 0
    
    # Função de apresentação inicial
    apresentacao()
    
    # Obtendo a quantidade de leitura
    qtdanalise = obter_quantidade_de_analise()
    
    # Lendo os valores
    vetor_analise = leitura_dos_dados(qtdanalise)
    
    # Apresentando os valores lidos
    apresentacao_dos_dados(vetor_analise, qtdanalise = qtdanalise)
    
    # Confirmando os valores lidos
    vetor_analise = confirmacao_dos_dados(qtdanalise, vetor_analise)
    
    # Incremento do contador de conjuntos e elementos para apresentação final
    total_conjuntos += 1
    total_elementos += qtdanalise
    
    # Efetuando a análise
    total_conjuntos, total_outliers, total_elementos, sensibilidade = analisar_dados(vetor_analise, qtdanalise, None, total_conjuntos, total_outliers, total_elementos)
    
    # Apresentando o menu de escolha
    opcao_menu = menu_escolha()
    
    # Loop para o menu
    while opcao_menu != "4":
        total_conjuntos, total_outliers, total_elementos, sensibilidade = escolha_do_menu(opcao_menu, total_conjuntos, total_outliers, total_elementos, sensibilidade, vetor_analise, qtdanalise)
        opcao_menu = 0
        opcao_menu = menu_escolha()
    
    # Resumo final
    limpar_tela()
    print("----- RESUMO DA SESSÃO -----")
    print()
    print(f"Conjuntos analisados: {total_conjuntos}")
    print(f"Total de números processados: {total_elementos}")
    print(f"Total de outliers detectados: {total_outliers}")
    print()
    print("Obrigado por utilizar o Detector de Outliers!")
    print()

main()