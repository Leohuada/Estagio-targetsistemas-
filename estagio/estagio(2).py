def pertence_a_fibonacci(numero):
    # Inicializando os primeiros valores da sequência de Fibonacci
    fib1, fib2 = 0, 1

    # Verificando diretamente os casos base
    if numero == fib1 or numero == fib2:
        return f"O número {numero} pertence à sequência de Fibonacci."

    # Calculando a sequência de Fibonacci até o número informado
    while fib2 < numero:
        fib1, fib2 = fib2, fib1 + fib2

    # Verificação se o número informado pertence à sequência
    if fib2 == numero:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} NÃO pertence à sequência de Fibonacci."

# Número a ser verificado
numero = int(input("Informe um número: "))
resultado = pertence_a_fibonacci(numero)
print(resultado)
