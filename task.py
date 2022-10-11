answer = ""
a, b, c = list(map(int, input().split()))

D = b ** 2 - 4 * a * c

if D < 0:
    answer = "Нет корней"
elif D == 0:
    answer = str(-b/(a * 2))
else:
    root_1 = (-b + D ** 0.5)/(a * 2)
    root_2 = (-b - D ** 0.5)/(a * 2)
    answer = str(root_1) + " " + str(root_2)

print(answer)