
#Função números primos
def findPrime(number):
    if number <= 1:
        return False
    else:
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True


def primeLinear(limit):
    if limit <= 1:
        return []
    primes = []
    for number in range (2, limit + 1):
        if findPrime(number):
            primes.append(number)
    return primes


def primeRecursive(limit, number=2, primes=None):
    if primes is None:
        primes = [] 

    if number > limit: 
        return primes

    if findPrime(number):  
        primes.append(number)

    return primeRecursive(limit, number + 1, primes)

#Testes

print("correto" if primeLinear(2) == [2] else "errado")
print("correto" if primeLinear(3) == [2, 3] else "errado")
print("correto" if primeLinear(10) == [2, 3, 5, 7] else "errado")

print("correto" if primeRecursive(2) == [2] else "errado")
print("correto" if primeRecursive(3) == [2, 3] else "errado")
print("correto" if primeRecursive(10) == [2, 3, 5, 7] else "errado")




# Função fibonacci
def fibonacciRecursive(number):
    if number < 0:
        raise ValueError("O número deve ser maior ou igual a 0.")
    if number == 0:
        return 0
    if number == 1:
        return 1
    
    #Somando dois valores anteriores na sequência após checar os casos base.
    return fibonacciRecursive(number - 1) + fibonacciRecursive(number - 2)


def fibonacciLinear(number):
    if number < 0:
        raise ValueError("O número deve ser maior ou igual a 0.")
    if number == 0:
        return 0
    if number == 1:
        return 1

    # ps1: Teoricamente essa função seria mais eficiente pelo uso de um loop único.
    # ps2: Decidi não fazer uma função que resolva os casos base exclusivamente por conta de legibilidade.
    prev1, prev2 = 0, 1
    for i in range(2, number + 1):
        current = prev1 + prev2
        prev1, prev2 = prev2, current

    return current

#Testes 
print("correto" if fibonacciRecursive(3) == 2 else "errado")
print("correto" if fibonacciRecursive(4) == 3 else "errado")
print("correto" if fibonacciRecursive(5) == 5 else "errado")

print("correto" if fibonacciLinear(3) == 2 else "errado")
print("correto" if fibonacciLinear(4) == 3 else "errado")
print("correto" if fibonacciLinear(5) == 5 else "errado")

