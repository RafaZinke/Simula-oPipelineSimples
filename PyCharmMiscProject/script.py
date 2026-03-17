def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

def calculadora():
    print("=" * 30)
    print("      CALCULADORA SIMPLES")
    print("=" * 30)

    while True:
        print("\nOperações disponíveis:")
        print("  1 - Soma")
        print("  2 - Subtração")
        print("  3 - Multiplicação")
        print("  4 - Divisão")
        print("  0 - Sair")

        opcao = input("\nEscolha uma operação: ").strip()

        if opcao == "0":
            print("\nAté logo!")
            break

        if opcao not in ("1", "2", "3", "4"):
            print("Opção inválida. Tente novamente.")
            continue

        try:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Digite apenas números.")
            continue

        if opcao == "1":
            resultado = somar(a, b)
            operador = "+"
        elif opcao == "2":
            resultado = subtrair(a, b)
            operador = "-"
        elif opcao == "3":
            resultado = multiplicar(a, b)
            operador = "×"
        elif opcao == "4":
            resultado = dividir(a, b)
            operador = "÷"

        print(f"\nResultado: {a} {operador} {b} = {resultado}")

if __name__ == "__main__":
    calculadora()