import sqlite3

## conect the sql
connection = sqlite3.connect("student.db")


# Create a cursor object to insert record, craete table, retreeve 
cursor =connection.cursor()

## create the table 

table_info = """
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT);

"""


cursor.execute(table_info)


# inser some more recordes

cursor.execute('''Insert into STUDENT values('Nasir','data Science', 'A', 90)''')
cursor.execute('''Insert into STUDENT values('Akhtar','Generative AI', 'B', 87)''')
cursor.execute('''Insert into STUDENT values('Asad','DEVOPS', 'A', 83)''')
cursor.execute('''Insert into STUDENT values('Munawer','data Science', 'C', 93)''')
cursor.execute('''Insert into STUDENT values('Muzafar','Generative AI', 'A', 83)''')
cursor.execute('''Insert into STUDENT values('Ali','DEVOPS', 'C', 82)''')
cursor.execute('''Insert into STUDENT values('Kashif','data Science', 'A', 79)''')
cursor.execute('''Insert into STUDENT values('Aneela','DEVOPS', 'B', 81)''')
cursor.execute('''Insert into STUDENT values('Danish','data Science', 'A', 78)''')
cursor.execute('''Insert into STUDENT values('Rabia','DEVOPS', 'C', 82)''')
cursor.execute('''Insert into STUDENT values('Khizar','Generative AI', 'A', 76)''')
cursor.execute('''Insert into STUDENT values('Nazia','data Science', 'A', 73)''')#
cursor.execute('''Insert into STUDENT values('Bilal','Generative AI', 'B', 72)''')
cursor.execute('''Insert into STUDENT values('sajid','DEVOPS', 'A', 87)''')
cursor.execute('''Insert into STUDENT values('Asif','data Science', 'C', 63)''')
cursor.execute('''Insert into STUDENT values('Husnain','Generative AI', 'A', 98)''')
cursor.execute('''Insert into STUDENT values('Hamza','DEVOPS', 'C', 84)''')
cursor.execute('''Insert into STUDENT values('Ikram','data Science', 'A', 65)''')
cursor.execute('''Insert into STUDENT values('Ramzan','DEVOPS', 'B', 78)''')
cursor.execute('''Insert into STUDENT values('Abid','data Science', 'A', 72)''')
cursor.execute('''Insert into STUDENT values('Jafir','DEVOPS', 'C', 81)''')
cursor.execute('''Insert into STUDENT values('Sadiq','Generative AI', 'A', 92)''')


## Display all the recards
print("The inserted recards are")

data = cursor.execute('''Select * From STUDENT''')

for row in data:
    print(row)
    
    
# close the connection 
connection.commit()
connection.close()