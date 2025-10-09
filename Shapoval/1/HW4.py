N = int(input("Введіть значення N: "))
a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
c = int(input("Введіть третє число: "))

numbers = [a, b, c]
valid_numbers = [num for num in numbers if 1 <= num <= N]

#результат
if valid_numbers:
    print("Числа що належать інтервалу [1; N]: ", valid_numbers)
else:
    print("Жодне з чисел не належить інтервалу [1; N].")
