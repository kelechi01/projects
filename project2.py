import sqlite3 

con = sqlite3.connect('test.db')
cu = con.cursor()

# inserting values
cu.execute("INSERT INTO result VALUES('chinwendu', 'oguejiofor',78)")

print('chinwendu')
con.commit()
con.close()