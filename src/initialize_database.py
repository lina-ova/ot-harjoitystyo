from database_connection import get_database_connection

def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE if exists riddles;
    ''')
    cursor.execute('''
    DROP TABLE if exists hunters;''')

    connection.commit()


def create_riddles(connection):
    cursor = connection.cursor()

    with open('data/riddles.sql', 'r') as riddles_file:
        sql_scrip=riddles_file.read()
    cursor.executescript(sql_scrip)

    connection.commit()

def create_history(connection):
    cursor=connection.cursor()
    with open('data/hunters.sql', 'r') as hunters_file:
        sql_sqript=hunters_file.read()
    cursor.executescript(sql_sqript)
    connection.commit()



def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_riddles(connection)
    create_history(connection)


if __name__ == "__main__":
    initialize_database()