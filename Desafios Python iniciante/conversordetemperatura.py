def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

escolha = input("Escolha a conversão (1: Celsius para Fahrenheit, 2: Fahrenheit para Celsius): ")

if escolha == '1':
    celsius = float(input("Digite a temperatura em Celsius: "))
    print(f"A temperatura em Fahrenheit é: {celsius_para_fahrenheit(celsius)}")
elif escolha == '2':
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    print(f"A temperatura em Celsius é: {fahrenheit_para_celsius(fahrenheit)}")
else:
    print("Opção inválida")
