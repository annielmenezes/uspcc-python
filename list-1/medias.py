from functools import reduce

notas = []

notas.append(int(input("Digite a primeira nota: ")))
notas.append(int(input("Digite a segunda nota: ")))
notas.append(int(input("Digite a terceira nota: ")))
notas.append(int(input("Digite a quarta nota: ")))

media = reduce((lambda x, y: x + y), notas) / len(notas)

print("A média aritmética é", media)
