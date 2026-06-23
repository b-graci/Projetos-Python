def calculadora(n1, n2, operacao):

    if operacao == 1:
        return n1 + n2

    elif operacao == 2:
        return n1 - n2

    elif operacao == 3:
        return n1 * n2

    elif operacao == 4:
        return n1 / n2

    else:
        return 0


operacao = int(input(
    "Digite a operação:\n"
    "1 - Adição\n"
    "2 - Subtração\n"
    "3 - Multiplicação\n"
    "4 - Divisão\n"
    "0 - Sair\n"
))

while operacao != 0:

    if operacao < 1 or operacao > 4:
        print("Opção inválida!")
    else:
        numeros = input("Digite dois números (ex: 23,40): ")
        lista = numeros.split(",")

        n1 = float(lista[0])
        n2 = float(lista[1])

        resultado = calculadora(n1, n2, operacao)
        print("Resultado do cálculo:", resultado)

    operacao = int(input(
        "\nDigite a operação novamente:\n"
        "1 - Adição\n"
        "2 - Subtração\n"
        "3 - Multiplicação\n"
        "4 - Divisão\n"
        "0 - Sair\n"
    ))