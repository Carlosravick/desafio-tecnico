def verifica_fibonacci(numero):

    if numero < 0:
        return False
    
    a, b = 0, 1
    

    if numero == a:
        return True
    
  
    while b <= numero:
        if b == numero:
            return True
        a, b = b, a + b  
    
    return False


numero = int(input("Informe um número para verificar: "))


if verifica_fibonacci(numero):
    print(f"O número {numero} PERTENCE à sequência de Fibonacci!")
else:
    print(f"O número {numero} NÃO PERTENCE à sequência de Fibonacci!")