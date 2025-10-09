from datetime import datetime

initial_price = 2000000  # грн


year_of_manufacture = int(input("Введіть рік випуску автомобіля: "))
current_mileage = int(input("Введіть пробіг автомобіля (у км): "))

current_year = datetime.now().year


age_of_car = current_year - year_of_manufacture
depreciation = age_of_car * 0.1
final_price = initial_price * (1 - depreciation)


if age_of_car > 0:  # Уникнення ділення на нуль
    average_annual_mileage = current_mileage / age_of_car
else:
    average_annual_mileage = current_mileage

print(f"Інформація про автомобіль:")
print(f"- Рік випуску: {year_of_manufacture}")
print(f"- Вік автомобіля: {age_of_car} років")
print(f"- Первісна вартість: {initial_price} грн")
print(f"- Пробіг автомобіля: {current_mileage} км")
print(f"- Середній річний пробіг: {average_annual_mileage:.0f} км/рік")
print(f"- Орієнтовна поточна вартість: {final_price:.2f} грн")

