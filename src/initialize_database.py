from database_connection import get_database_connection

def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE if exists riddles;
    ''')

    connection.commit()


def create_riddles(connection):
    cursor = connection.cursor()

    with open('data/riddles.sql', 'r') as riddles_file:
        sql_scrip=riddles_file.read()
    cursor.executescript(sql_scrip)

    connection.commit()



def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_riddles(connection)


if __name__ == "__main__":
    initialize_database()