qtd = int(input())
case = []
for i in range(qtd):
    case.append(input())

for i in range(qtd):
    nOpenDiamonds = 0
    count = 0
    for c1 in case[i]:
        if (c1 == "<"):
            nOpenDiamonds += 1
        if (c1 == ">" and nOpenDiamonds > 0):
            nOpenDiamonds -= 1
            count += 1
    print(count)
