import random

def ler_pontos_arquivo():
    try:
        with open("nomes.txt", "r", encoding="latin1") as nomes:
            pontos = nomes.read().splitlines()
        return pontos
    except FileNotFoundError:
        print("Arquivo de pontos não encontrado.")
        return []


def salvar_pontos_arquivo(pontos):
    with open("nomes.txt", "w", encoding="latin1") as nomes:
        for ponto in pontos:
            nomes.write(ponto + "\n")

def exibir_menu():
    print("Menu:")
    print("1. Carregar pontos")
    print("2. Definir valor do ponto")
    print("3. Definir taxa de administração")
    print("4. Calcular valor arrecadado")
    print("5. Definir quantidade de prêmios")
    print("6. Realizar sorteio")
    print("7. Resetar rifa")
    print("8. Exibir dados gerais")
    print("9. Sair")

def carregar_pontos():
    pontos = ler_pontos_arquivo()
    if pontos:
        print("Pontos carregados com sucesso.")
    else:
        print("Nenhum ponto cadastrado.")
    return pontos

def definir_valor_do_ponto():
    valor_ponto = float(input("Digite o valor do ponto da rifa: "))
    return valor_ponto

def definir_taxa_de_administracao():
    taxa_administracao = float(input("Digite a taxa de administração da rifa em porcentagem: "))
    return taxa_administracao

def calcular_valor_arrecadado(pontos, valor_ponto, taxa_administracao):
    total_arrecadado = len(pontos) * valor_ponto
    valor_liquido = total_arrecadado * (taxa_administracao / 100)
    valor_taxa_administracao = total_arrecadado - valor_liquido
    print(f"Valor arrecadado: R${total_arrecadado:.2f}")
    print(f"Valor líquido: R${valor_liquido:.2f}")
    print(f"Taxa de administração: R${valor_taxa_administracao:.2f}")

def definir_quantidade_de_premios():
    quantidade_premios = int(input("Digite a quantidade de prêmios a serem sorteados: "))
    return quantidade_premios

def realizar_sorteio(pontos, quantidade_premios):
    if len(pontos) < quantidade_premios:
        print("Quantidade de prêmios maior que a quantidade de pontos vendidos.")
        return
    sorteados = random.sample(pontos, quantidade_premios)
    print("Números sorteados e nomes correspondentes:")
    for sorteado in sorteados:
        numero = pontos.index(sorteado) + 1
        print(f"Número: {numero} - Nome: {sorteado}")

def resetar_rifa():
    pontos = ['-'] * len(pontos)
    salvar_pontos_arquivo(pontos)
    print("A rifa foi resetada.")

def exibir_dados_gerais_da_rifa(pontos):
    pontos_disponiveis = pontos.count('-')
    pontos_vendidos = len(pontos) - pontos_disponiveis
    nao_vendidos = [ponto for ponto in pontos if ponto == '-']
    print(f"Quantidade de pontos disponíveis: {pontos_disponiveis}")
    print(f"Quantidade de pontos vendidos: {pontos_vendidos}")
    print(f"Não vendidos: {nao_vendidos}")
    print(f"Lista de pontos vendidos: {pontos}")
    print(f"Lista de pontos não vendidos: {nao_vendidos}")

def main():
    pontos = []
    valor_ponto = 0
    taxa_administracao = 0
    quantidade_premios = 0

    while True:
        exibir_menu()
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            pontos = carregar_pontos()
        elif opcao == 2:
            valor_ponto = definir_valor_do_ponto()
        elif opcao == 3:
            taxa_administracao = definir_taxa_de_administracao()
        elif opcao == 4:
            calcular_valor_arrecadado(pontos, valor_ponto, taxa_administracao)
        elif opcao == 5:
            quantidade_premios = definir_quantidade_de_premios()
        elif opcao == 6:
            realizar_sorteio(pontos, quantidade_premios)
        elif opcao == 7:
            resetar_rifa()
        elif opcao == 8:
            exibir_dados_gerais_da_rifa(pontos)
        elif opcao == 9:
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
