def calculadora():
    operacao = input("Escolha a operação (+, -, *, /): ")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if operacao == '+':
        print(f"Resultado: {num1 + num2}")
    elif operacao == '-':
        print(f"Resultado: {num1 - num2}")
    elif operacao == '*':
        print(f"Resultado: {num1 * num2}")
    elif operacao == '/':
        print(f"Resultado: {num1 / num2}")
    else:
        print("Operação inválida")

calculadora()