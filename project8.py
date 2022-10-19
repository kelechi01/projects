import sqlite3

con = sqlite3.connect('test.db')
cu = con.cursor()

new = [('ifeanyi', 'obi', 93),('chima', 'steph', 85),('joseph', 'emma', 69),('emmanuel', 'chinonso', 93),('sopuruchi', 'amanda', 73),('nmesoma', 'obinna', 74)]
cu.executemany("INSERT INTO result VALUES(?,?,?)", new)
print('you')
con.commit()
con.close()