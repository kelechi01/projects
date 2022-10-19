import sqlite3

con = sqlite3.connect('test.db')
cu = con.cursor()
# cu.execute("SELECT * FROM result WHERE first_name = 'chinwendu' ")
cu.execute("SELECT * FROM result WHERE first_name LIKE 'ch%' ")

p = cu.fetchall()
print(p)


con.commit()
con.close() 