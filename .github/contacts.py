#contats
import datetime
import sqlite3

def delete(wanted_last,wanted_name):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    delet = f'DELETE from contacts where First_name =?  and Last_name = ?'
    print('done')
    cursor.execute(delet,  (wanted_last,wanted_name))
    conn.commit()

print('''Hi welcome to my app this app let u to save your telefon numbers
if you want to add sombody to your contacts write \'add\'or delete sombody write \'delete\'.
Or you can search with 'search' by name and last name.\n''')

darkhast = input('What can i do for you? (add, delete, search) (: ')
if darkhast == 'add':
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    First_name = input('Name: ').lower()
    Last_name = input('Last name: ').lower()
    Telefon = int(input('Telefon number: '))
    Time = datetime.datetime.now()
    queri_1 = f'insert into contacts values(?, ?,?,?)'
    cursor.execute(queri_1,   (First_name,Last_name,Time ,Telefon))
    conn.commit()
    cursor.close()
elif darkhast == 'delete':
   wanted_last = input('Write Lastname :) ')
   wanted_name = input('Write Firstname :) ')
   delete(wanted_name,wanted_last)
elif darkhast == 'search':
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    wanted_n = input('tell me name')
    wanted_f = input('Tell me lastname ?:) ')
    query = f'select * from contacts where First_name = ? and Last_name = ? '
    c.execute(query,  (wanted_n,wanted_f))
    print()
    conn.commit()
    conn.close()

