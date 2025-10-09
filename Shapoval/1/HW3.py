import math

x = float(input("Введіть значення x: "))

#обчислення
if x >= 0:
    f = 0.5 - math.pow(abs(x), 1/4)   # 0.5 - 4-й корінь з |x|
else:
    denominator = abs(x + 1)
    if denominator == 0:
        print("Помилка: знаменник дорівнює нулю.")
        exit()
    f = (math.sin(x**2))**2 / denominator

#виведення результату з точністю до 2 знаків після коми
print(f"f(x) = {f:.2f}")
