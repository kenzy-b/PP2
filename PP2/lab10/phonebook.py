import psycopg2
import csv
import os

# Подключение к базе данных
conn = psycopg2.connect(
    dbname="phonebook",
    user="postgres",
    password="010706",
    host="localhost",
    client_encoding="utf8"
)

cur = conn.cursor()

def patternSearch():
    pattern = input("Write pattern: ")
    cur.execute("Select * from patternSearch(%s)", (pattern,))
    print(cur.fetchall())

def insert_or_update():
    name = input("name: ")
    phone = input("phone: ")
    cur.execute("CALL insert_or_update(%s, %s)", (name, phone))
    conn.commit()
    print("Successfully added/updated!")

def manyUsers():
    n = int(input("How many users you want to add? "))
    names = []
    phones = []

    for _ in range(n):
        name = input("name: ")
        phone = input("phone: ")
        names.append(name)
        phones.append(phone)

    cur.execute("Call manyUsers(%s, %s)", (names, phones))
    conn.commit()
    print(f"Successfully added {n} users!")

def pagination():
    limit = int(input("How many rows do you want to display? "))
    offset = int(input("Where do we start from? "))
    cur.execute("Select * from pagination(%s, %s)", (limit, offset))
    print(cur.fetchall())

def deletion():
    nameOrPhone = input("Enter a name or phone number: ")
    cur.execute("Call deletion(%s)", (nameOrPhone,))
    conn.commit()
    print("Successfully deleted!")

def import_from_csv():
    filename = r"C:\Users\bayan\OneDrive\Desktop\PP2\lab10\data.csv"
    if not os.path.exists(filename):
        print(f"❌ Error: File '{filename}' not found in the current directory!")
        return

    try:
        with open(filename, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            next(reader) 
            
            success_count = 0
            for row in reader:
                if len(row) != 2:
                    print(f"⚠ Skipping invalid row: {row}")
                    continue

                name, phone = row
                cur.execute("CALL insert_or_update(%s, %s)", (name.strip(), phone.strip()))
                success_count += 1

            conn.commit()
            print(f"✅ Successfully imported {success_count} records from '{filename}'!")

    except Exception as e:
        print(f"❌ Error during CSV import: {e}")

while True:
    print("\n1. Search by pattern")
    print("2. Add or update a single user")
    print("3. Add 2 or more users")
    print("4. Pagination")
    print("5. Delete a user")
    print("6. Import from CSV (data.csv)")
    print("7. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        patternSearch()
    elif choice == "2":
        insert_or_update()
    elif choice == "3":
        manyUsers()
    elif choice == "4":
        pagination()
    elif choice == "5":
        deletion()
    elif choice == "6":
        import_from_csv()
    elif choice == "7":
        break
    else:
        print("Invalid choice")

cur.close()
conn.close()
