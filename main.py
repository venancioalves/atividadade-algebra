def solicitar_dimensoes():
    """Solicita as dimensões da matriz ao usuário."""
    linhas = int(input("Digite o número de linhas: "))
    colunas = int(input("Digite o número de colunas: "))
    return linhas, colunas

def criar_matriz(linhas, colunas):
    """Cria e retorna uma matriz baseada nas dimensões fornecidas pelo usuário."""
    matriz = []
    print("Digite os valores linha por linha:")

    for _ in range(linhas):
        linha = [int(input()) for _ in range(colunas)]
        matriz.append(linha)

    return matriz

def localizar_pivo(matriz, inicio):
    """Localiza o pivô e retorna sua posição (linha, coluna) e o valor."""
    for coluna in range(inicio, len(matriz[0])):
        for linha in range(inicio, len(matriz)):
            if matriz[linha][coluna] != 0:
                return linha, coluna, matriz[linha][coluna]
    return None, None, None

def executar_escalonamento(matriz):
    """Transforma a matriz em forma escalonada reduzida por linhas."""
    for i in range(len(matriz)):
        linha_pivo, coluna_pivo, valor_pivo = localizar_pivo(matriz, i)

        if coluna_pivo is None:
            break

        if linha_pivo != i:
            trocar_linhas(matriz, i, linha_pivo)
            exibir_etapa(f"Troca da linha {i + 1} com a linha {linha_pivo + 1}.", matriz)

        if valor_pivo != 1:
            multiplicar_linha(matriz, i, 1 / valor_pivo)
            exibir_etapa(f"Multiplicando a linha {i + 1} por {round(1 / valor_pivo, 2)}.", matriz)

        for linha_abaixo in range(i + 1, len(matriz)):
            fator = matriz[linha_abaixo][coluna_pivo]
            if fator != 0:
                somar_linhas(matriz, linha_abaixo, i, -fator)
                exibir_etapa(f"Zerando o elemento abaixo do pivô na linha {linha_abaixo + 1}.", matriz)

        for linha_acima in range(i - 1, -1, -1):
            fator = matriz[linha_acima][coluna_pivo]
            if fator != 0:
                somar_linhas(matriz, linha_acima, i, -fator)
                exibir_etapa(f"Zerando o elemento acima do pivô na linha {linha_acima + 1}.", matriz)

def trocar_linhas(matriz, linha1, linha2):
    """Troca duas linhas da matriz."""
    matriz[linha1], matriz[linha2] = matriz[linha2], matriz[linha1]

def multiplicar_linha(matriz, linha, fator):
    """Multiplica uma linha da matriz por um fator."""
    matriz[linha] = [elemento * fator for elemento in matriz[linha]]

def somar_linhas(matriz, linha_destino, linha_origem, fator):
    """Soma uma linha multiplicada por um fator a outra linha."""
    matriz[linha_destino] = [
        destino + fator * origem
        for destino, origem in zip(matriz[linha_destino], matriz[linha_origem])
    ]

def exibir_etapa(mensagem, matriz):
    """Exibe a matriz com uma mensagem após cada etapa."""
    print(mensagem)
    imprimir_matriz(matriz)
    print("-" * 60)

def imprimir_matriz(matriz):
    """Imprime a matriz de forma formatada."""
    colunas_largura = [max(len(str(celula)) for celula in coluna) for coluna in zip(*matriz)]
    print("")
    for linha in matriz:
        print("| " + " | ".join(f"{str(celula).rjust(colunas_largura[i])}" for i, celula in enumerate(linha)) + " |")
    print("")

def main():
    """Função principal que controla o fluxo do programa."""
    while True:
        print("=" * 30)
        print("Bem-vindo, crie sua matriz")
        print("=" * 30)
        
        linhas, colunas = solicitar_dimensoes()
        if linhas == 0 or colunas == 0:
            print("Matriz inválida. Encerrando.")
            break

        matriz = criar_matriz(linhas, colunas)
        
        print("Essa é sua matriz:")
        imprimir_matriz(matriz)
        print("-" * 60)
        
        executar_escalonamento(matriz)
        print("Forma escalonada reduzida por linhas:")
        imprimir_matriz(matriz)
        
        print("=" * 60)
        
        opcao = input("Continuar? (S/N)").strip().lower()
        if opcao == "n":
            break

if __name__ == "__main__":
    main()
