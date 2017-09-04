import math

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = b ** 2 - (4 * a * c)


if delta < 0:
    print("esta equação não possui raízes reais")
elif delta == 0:
    x1 = (- b + math.sqrt(delta)) / 2 * a
    print("a raiz desta equação é", x1)
else:
    x1 = (- b + math.sqrt(delta)) / 2 * a
    x2 = (- b - math.sqrt(delta)) / 2 * a
    if x1 < x2:
        print("as raízes da equação são "+ str(x1) +" e "+ str(x2))
