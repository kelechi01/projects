import sqlite3
con = sqlite3.connect('test.db')
cu = con.cursor()

cu.execute(" DELETE from result WHERE last_name = 'amaka' ")
cu.execute(" DELETE from result WHERE rowid = 4 ")

print('come')
con.commit()
con.close()