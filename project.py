import sqlite3

con = sqlite3.connect('test.db')
cu = con.cursor()
cu.execute('''CREATE TABLE result(
    first_name text,
    last_name text,
    score integer
)''')
print('hg')


con.commit()
con.close()