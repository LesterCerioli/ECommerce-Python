
class Query:

    cursor = cnxn.cursor()
    cursor.execute('SELECT * FROM usuarios')
    rows = cursor.fetchall()
