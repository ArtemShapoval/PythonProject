import math

#введення даних
x = int(input("Введіть останню цифру номера у списку групи (x): "))
t = 1  # умова задачі

numerator = 9 * math.pi * t + 10 * math.cos(x)
denominator = math.sqrt(t) - abs(math.sin(t))

#перевірка на нуль в дільнику
if denominator == 0:
    print("Помилка: знаменник дорівнює нулю.")
else:
    Z = (numerator / denominator) * math.exp(x)
    #виведення з точністю до 2 знаків після коми
    print(f"Результат: Z = {Z:.2f}")
