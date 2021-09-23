import sqlite3
conn = sqlite3.connect('1.db')
cursor = conn.cursor()

i = 0
while i <2 :
    first_name = input('esmeto bgoo: ')
    last_name = input('familit bgo: ')
    age = int(input('chand salete: '))
    score = int(input('nomrat chan shod: '))
    kelas = input('che kelasi miri: ')
    query = f"insert into students2 values('{first_name}', '{last_name}','{age}', '{score}','{kelas}')"
    cursor.execute(query)
    i+=1
conn.commit()
