def gerar_tabuada(numero):
    resultados = []
    for i in range(1, 11):
        resultados.append(numero * i)
    return resultados


if __name__ == "__main__":
    numero = int(input("Digite o número: "))
    tabuada = gerar_tabuada(numero)

    for i, resultado in enumerate(tabuada, start=1):
        print(f"{numero} * {i} = {resultado}")