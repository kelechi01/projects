import sqlite3

con = sqlite3.connect('church.db')
cu =con.cursor()
# cu.execute("""
#     CREATE TABLE data(
#         First_name text,
#         Last_name text,
#         Email text,
#         Username text,
#         password text
#      )""")

cu.execute("INSERT INTO data VALUES ('Chinwendu', 'vivian', 'chinwenduoguejiofor9@gmail.com', 'Chinweogu','kele1234')")

print('you')
con.commit()
con.close()