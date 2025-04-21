import csv
import psycopg2 as pgsql

# Подключение к базе данных
connection = pgsql.connect(host="localhost", dbname="phonebook", user="postgres", 
                            password="010706")
cur = connection.cursor()

# Создание таблицы с полем id
cur.execute("""
    CREATE TABLE IF NOT EXISTS PhoneBook (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        phone VARCHAR(20)
    );
""")

# Функция обновления данных
def update(id, mode, newv):
    query = f"UPDATE PhoneBook SET {mode} = %s WHERE id = %s"
    cur.execute(query, (newv, id))

# Функция удаления данных
def delete(id):
    query = "DELETE FROM PhoneBook WHERE id = %s"
    cur.execute(query, (id,))

# Вставка данных вручную
while True:
    print("Type 'enter' if you want to add more data and type 'stop' to break")
    mode = input()
    if mode == "stop":
        break

    name = input("Enter name: ")
    phone = input("Enter phone: ")

    cur.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)",
                (name, phone))

# Вставка данных из CSV
while True:
    print("Want to insert data from csv file? yes/no:")
    mode = input()
    if mode == "no":
        break
    print("Enter the name of the file")
    filename = input()

    with open(filename + '.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Пропустить заголовок
        for row in reader:
            cur.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", row)

# Обновление данных
while True:
    print("Type 'update' to update some data or 'stop' to break")
    mode = input()
    if mode == "stop":
        break

    cur.execute("SELECT * FROM PhoneBook")
    print(cur.fetchall())

    id_to_change = input("Enter id: ")
    column_to_change = input("What you want to change? name/phone: ")
    new_value = input("Enter new name/phone: ")

    update(id_to_change, column_to_change, new_value)

# Удаление данных
while True:
    print("Want to delete some data? yes/no")
    mode = input()
    if mode == "no":
        break

    cur.execute("SELECT * FROM PhoneBook")
    print(cur.fetchall())

    id_to_delete = input("Enter id: ")
    delete(id_to_delete)

# Сохранение изменений и закрытие соединения
connection.commit()
cur.close()
connection.close()





