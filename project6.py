import sqlite3

con = sqlite3.connect('test.db')
cu = con.cursor()

# cu.execute(
#     """ UPDATE result SET first_name = 'Chidi'
#                 WHERE last_name= 'oluchi'
#      """
# )
# cu.execute("""
#         SELECT  rowid, * FROM result
# """)
# print('you')

cu.execute(
    """
        UPDATE result SET last_name = 'amaka'
        WHERE rowid = 3
    """
)

con.commit()
con.close()