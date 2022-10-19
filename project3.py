import sqlite3

con = sqlite3.connect('test.db')
cu = con.cursor()

lst = [('chizaram', 'oluchi', 89),('David', 'Kingpaulo', 92),('Amara','Osinach', 79),('Prosper', 'Emeka', 90)]
cu.executemany("INSERT INTO result VALUES (?,?,?) ", lst)


con.commit()
con.close()