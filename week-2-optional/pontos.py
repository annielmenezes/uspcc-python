x1 = int(input("Digite o primeiro ponto x: "))
y1 = int(input("Digite o primeiro ponto y: "))
x2 = int(input("Digite o segundo ponto x: "))
y2 = int(input("Digite o segundo ponto y: "))



distance = (((x1 - y1) ** 2) + ((x2 - y2) ** 2)) ** 2

if distance >= 10:
    print("longe")
else:
    print("perto")
