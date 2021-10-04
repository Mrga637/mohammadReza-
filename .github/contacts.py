#contats
import datetime
import sqlite3

def delete(wanted_last,wanted_name):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    #delet = f'DELETE from contacts where First_name =?  and Last_name = ?'
    print('done')
    cursor.execute(f'DELETE from contacts where First_name =?  and Last_name = ?',  (wanted_last,wanted_name))
    conn.commit()

print('''***Hi welcome to my app this app let u to save your telefon numbers
if you want to add sombody to your contacts write \'add\'or delete sombudy write \'delete\'.
Or you can search with 'search' by name and last name.***\n''')
while 1==1 :
   darkhast = input('What can i do for you? (add, delete, search) (: ').lower()
   if darkhast == 'add':
     conn = sqlite3.connect('data.db')
     cursor = conn.cursor()
     First_name = input('Name: ').lower()
     Last_name = input('Last name: ').lower()
     Telefon = int(input('Telefon number: '))
     Time = datetime.datetime.now()
   # queri_1 = f'insert into contacts values(?, ?,?,?)'
     cursor.execute(f'insert into contacts values(?, ?,?,?)',   (First_name,Last_name,Time ,Telefon))
     conn.commit()
     cursor.close()
     print('Done(:')

   elif darkhast == 'delete':
      wanted_last = input('Write Lastname :) ').lower()
      wanted_name = input('Write Firstname :) ').lower()
      delete(wanted_name,wanted_last)
      print('Done(:')
   elif darkhast == 'search':
       conn = sqlite3.connect('data.db')
       c = conn.cursor()
       wanted_n = input('tell me name:').lower()
       wanted_f = input('Tell me lastname ?:) ').lower()
    #query = f'SELECT * from contacts where First_name=? and Last_name =? '
       c.execute(f'SELECT * from contacts where First_name=? and Last_name =? ',  (wanted_n,wanted_f))
       back = c.fetchall()
       for ba in back:
          print(ba)
       conn.commit()
       conn.close()
       print('Done(:')
   again = input('Do you want to do anything else?(yes\\no):').lower()
   if again =='yes': pass
   elif again == 'no' :break

