"""
10.17. Домашнее задание - Sets и словари
"""

books: dict[str, str] = {
    "Мастер и Маргарита": "Михаил Булгаков",
    "Идиот": "Фёдор Достоевский",
    "Преступление и наказание": "Фёдор Достоевский"
}

all_books: list[str] = []
all_autors: list[str] = []

for book, autor in books.items():
    all_books.append(book)
    all_autors.append(autor)

print(f"Список всех книг: {all_books}")
print(f"Список авторов: {set(all_autors)}")
