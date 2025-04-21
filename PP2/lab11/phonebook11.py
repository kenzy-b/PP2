import psycopg2

# Подключение к базе данных
conn = psycopg2.connect(
    dbname="phonebook",
    user="postgres",
    password="010706", 
    host="localhost",
)

cur = conn.cursor()

# Поиск по шаблону
pattern = input("Write pattern: ")
cur.execute("SELECT * FROM search_phonebook(%s)", (pattern,))
print(cur.fetchall())

# Вставка одного пользователя
cur.execute("CALL insert_or_update_user(%s, %s)", ('John', '+77001112233'))

# Вставка нескольких пользователей
names = ['Alice', 'Bob', 'Charlie']
phones = ['+77001234567', '1234', '+77007654321']
cur.execute("CALL insert_many_users(%s, %s)", (names, phones))


# Пагинация
cur.execute("SELECT * FROM get_phonebook_page(%s, %s)", (5, 0))  # 5 записей с 0-й страницы
print(cur.fetchall())

# Удаление
cur.execute("CALL delete_user(%s)", ('Alice',))

# Сохраняем изменения и закрываем соединение
conn.commit()
cur.close()
conn.close()
