import math

x1 = int(input("Digite o primeiro ponto x: "))
y1 = int(input("Digite o primeiro ponto y: "))
x2 = int(input("Digite o segundo ponto x: "))
y2 = int(input("Digite o segundo ponto y: "))

distance = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

if distance >= 10:
    print("longe")
else:
    print("perto")
