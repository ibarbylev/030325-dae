import mysql.connector
from pymongo import MongoClient
from datetime import datetime, UTC

# =============== local_settings.py ==================

MONGODB_URL_WRITE = ''
HOST = ''
USER = ''
PASSWORD = ''
DATABASE = ''

dbconfig = {
    'host': HOST,
    'user': USER,
    'password': PASSWORD,
    'database': DATABASE,
}

# =============== functions.py ==================
def add_log(collection, *args):
    doc = {
        "type": f"{' '.join(str(arg) for arg in args)}",
        "createdAt": datetime.now(UTC)
    }

    # Добавляем этот документ к текущей коллекции
    collection.insert_one(doc)


def print_genres(cursor):
    cursor.execute("SELECT category_id, name FROM category;")
    tables = cursor.fetchall()
    print("Список жанров в базе данных:")
    for t in tables:
        print(f"{t[0]}: {t[1]}")


def print_films_by_genres_and_page(cursor, genre, page=1):
    offset = (page - 1) * 10
    cursor.execute("""
                   SELECT f.title, fc.category_id
                   FROM film AS f
                            JOIN film_category AS fc USING (film_id)
                   WHERE fc.category_id = %s
                   LIMIT 10 OFFSET %s
                   """, (genre, offset))
    films = cursor.fetchall()
    print(f"\n--- Страница {page} ---")
    if not films:
        print("Нет фильмов на этой странице.")
    for t in films:
        print(t[0], f"(жанр: {t[1]})")

    # добавляем логирование
    add_log(collection, "поиск по жанру", genre)


# =============== main.py ==================

client = MongoClient(MONGODB_URL_WRITE)
db = client.ich_edit
collection = db.final_project_17022025_BAR
with mysql.connector.connect(**dbconfig) as connection:
    with connection.cursor() as cursor:
        print_genres(cursor)
        genre = int(input("Введите номер жанра: "))
        page = 1
        while True:
            print_films_by_genres_and_page(cursor, genre, page)
            print("\nНавигация: 1 - предыдущая, 2 - следующая, 3 - выход")
            n = input("Ваш выбор: ")
            if n == "3":
                break
            elif n == "1":
                if page > 1:
                    page -= 1
                else:
                    print("Вы уже на первой странице.")
            elif n == "2":
                page += 1
            else:
                print("Неверный ввод.")



client.close()

