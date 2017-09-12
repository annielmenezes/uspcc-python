n = int(input("Digite o valor de n: "))

double_n = n * 2
count = 0
while double_n > 0:
    if double_n % 2 != 0:
        print(count)
    count = count + 1
    double_n = double_n - 1
