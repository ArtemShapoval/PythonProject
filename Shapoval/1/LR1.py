# 1. Запит даних
user_input = input("Будь ласка, введіть список чисел, розділених комами: ")

# 2. Перетворення даних
numbers_list = [int(item) for item in user_input.split(',')]

# HW2. Сортування списку
numbers_list.sort()

# 4. Обрахунок медіани
# Визначаємо, чи кількість елементів у списку парна чи непарна
n = len(numbers_list)
if n % 2 == 1:
    # Непарна кількість чисел
    median = numbers_list[n // 2]
else:
    # Парна кількість чисел, обраховуємо середнє двох середніх чисел
    median = (numbers_list[n // 2 - 1] + numbers_list[n // 2]) / 2

# 5. Виведення результату
print(f"Медіана: {median}")

# Ініціалізація словника для зберігання даних про книги
books = {}
def add_book(books_dict):
    while True:
        book_input = input("Назва та автор(або 'stop'): ")
        if book_input.lower() == 'stop':
            break
        try:
            book, author = book_input.split(',', 1)
            books_dict[book.strip()] = author.strip()
        except ValueError:
            print("Некоректний ввід, спробуйте ще раз.")
    return books_dict

# 1. Введення даних про книги
def find_book_author(books_dict):
    book_to_find = input("Назву книги для пошуку автор: ")
    if book_to_find in books_dict:
        print(f"Автор книги '{book_to_find}': {books_dict[book_to_find]}")
    else:
        print("Книга не знайдена в базі даних.")

def main():
    books = {}
    while True:
        action = input("Виберіть дію: додати (a), видалити (r), переглянути (l), знайти автора (f), завершити (q): ")
        if action.lower() == 'a':
            books = add_book(books)
        elif action.lower() == 'r':
            books = remove_book(books)
        elif action.lower() == 'l':
            list_books(books)
        elif action.lower() == 'f':
            find_book_author(books)
        elif action.lower() == 'q':
            print("Програма завершена.")
            break
        else:
            print("Невідома команда, спробуйте ще раз.")



def remove_book(books_dict):
    book_to_remove = input("Введіть назву книги для видалення: ")
    if book_to_remove in books_dict:
        del books_dict[book_to_remove]
        print(f"Книга '{book_to_remove}' успішно видалена.")
    else:
        print("Книга не знайдена в базі даних.")
    return books_dict
def list_books(books_dict):
    if books_dict:
        print("Список всіх книг та їх авторів:")
        for book, author in books_dict.items():
            print(f"'{book}' автора {author}")
    else:
        print("База даних книг порожня.")


# HW2. Запит назви книги для пошуку автора
book_to_find = input("Введіть назву книги для пошуку її автора: ")

# 4. Виведення результату пошуку
if book_to_find in books:
    print(f"Автор книги '{book_to_find}': {books[book_to_find]}")
else:
    print("Книга не знайдена в базі даних.")

main()