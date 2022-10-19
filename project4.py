import sqlite3
con = sqlite3.connect('test.db')
cu = con.cursor()

cu.execute('SELECT rowid, * FROM result') 
a = (cu.fetchall())
for i in a:
    print(i)
# print(cu.fetchone()[1])
con.commit()
con.close()