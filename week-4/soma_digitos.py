digitos = int(input("Digite um número inteiro: "))

soma = 0

while digitos is not 0:
    soma   += digitos % 10
    digitos  = int(digitos / 10)

print(soma)
