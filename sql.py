
import sqlite3

## Connectt to SQlite
connection=sqlite3.connect("student.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

## create the table
table_info="""
Create table IF NOT EXISTS STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""
cursor.execute(table_info)

# Check if table is empty before inserting
cursor.execute("SELECT COUNT(*) FROM STUDENT")
count = cursor.fetchone()[0]

if count == 0:
    print("Inserting data into STUDENT table...")
    cursor.execute('''Insert Into STUDENT values('Ashu', 'Ocean Engineering', 'A', 100)''')
    cursor.execute('''Insert Into STUDENT values('Priyanshu', 'Civil Engineering', 'B', 85)''')
    cursor.execute('''Insert Into STUDENT values('Manan', 'Manufacturing Engineering', 'B', 90)''')
    cursor.execute('''Insert Into STUDENT values('Spandan', 'Architecture', 'A', 90)''')
    cursor.execute('''Insert Into STUDENT values('Aryan', 'Electronics Engineering', 'B', 87)''')
    cursor.execute('''Insert Into STUDENT values('Ayush', 'Mining Engineering', 'C', 75)''')
    cursor.execute('''Insert Into STUDENT values('Deepak', 'Civil Engineering', 'A', 95)''')
    print("Data inserted successfully!")
else:
    print(f"Table already has {count} records.")

## Disspaly ALl the records

print("The isnerted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()