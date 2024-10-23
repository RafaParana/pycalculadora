saida = ''

def adicao(num1, num2):
    return num1 + num2

def subracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return num1 / num2

def calculadora(num1, num2, operacao):
    if operacao in ['+', 'adição']:
        resultado = adicao(num1, num2)
    elif operacao in ['-', 'subtração']:
        resultado = subracao(num1, num2)
    elif operacao in ['*', 'multiplicação']:
        resultado = multiplicacao(num1, num2)
    elif operacao in ['/', 'divisão']:
        resultado = divisao(num1, num2)
    else:
        return "Operação inválida"
    
    return resultado

while saida.lower() != 'n':
    primeiro_numero = float(input("Digite o primeiro número: "))
    segundo_numero = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, / ou o nome da operação): ")

    resultado = calculadora(primeiro_numero, segundo_numero, operacao)
    
    print(f"Resultado da operação: {resultado}")
    
    saida = input("Deseja continuar? (S/N): ")
