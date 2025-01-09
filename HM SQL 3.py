import sqlite3

conn = sqlite3.connect("05.01.25 HM.db")

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE shopping (id INTEGER PRIMARY KEY, name TEXT, amount INTEGER);
''')

cursor.execute("INSERT INTO shopping VALUES (1, 'Avokado', 5);")
cursor.execute("INSERT INTO shopping VALUES (2, 'Milk', 2);")
cursor.execute("INSERT INTO shopping VALUES (3, 'Bread', 3);")
cursor.execute("INSERT INTO shopping VALUES (4, 'Chocolate', 8);")
cursor.execute("INSERT INTO shopping VALUES (5, 'Bamba', 5);")
cursor.execute("INSERT INTO shopping VALUES (6, 'Orange', 10);")

cursor.execute("SELECT * FROM shopping")
print("All items in shopping:")
print(cursor.fetchall())

cursor.execute("SELECT * FROM shopping WHERE amount > 5")
print("\nItems with amount > 5:")
print(cursor.fetchall())

cursor.execute("DELETE from shopping WHERE name like 'Orange'")

cursor.execute("UPDATE shopping SET name = 'Bisli' WHERE name LIKE 'Bamba'")

cursor.execute("UPDATE shopping SET amount=1 WHERE name LIKE 'Milk'")

cursor.execute("SELECT COUNT(*) FROM shopping")
print("\nTotal number of items in shopping:")
print(cursor.fetchall())

cursor.execute("SELECT * FROM shopping WHERE id > 0")
print("\nAll items where id > 0:")
print(cursor.fetchall())


conn.commit()
conn.close()
