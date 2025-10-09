from CsvToJsonConverter import CsvToJsonConverter
from JsonReader import JsonReader
from StudentFinder import StudentFinder

if __name__ == "__main__":
    # Шлях до CSV та JSON
    csv_url = "https://informer.com.ua/dut/python/import/st_gt.csv"
    json_path = "st_gt.csv"

    # 1. Конвертація з CSV у JSON
    converter = CsvToJsonConverter()
    converter.read_and_convert(csv_url, json_path)

    # 2. Читання даних з JSON
    json_reader = JsonReader()
    data = json_reader.read_data(json_path)

    # 3. Виведення всіх студентів (опціонально)
    print("\n===== Всі студенти з JSON =====")
    json_reader.display_data(json_path)

    # 4. Пошук студента за прізвищем
    finder = StudentFinder(json_reader)
    finder.load_data(json_path)

    surname_to_find = input("Ведіть прізвище: ")  # <- тут можеш змінити прізвище
    found_students = finder.find_students_by_surname(surname_to_find)
    finder.display_students_info(found_students)
    # . Виведення інформації про знайдених студентів




