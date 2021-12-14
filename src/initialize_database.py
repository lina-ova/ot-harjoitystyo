from database_connection import get_database_connection

def drop_tables(connection):
    """Poistaa tietokantataulut.
    Args:
        connection: Tietokantayhteyden Connection-olio"""
    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE if exists riddles;
    ''')
    cursor.execute('''
    DROP TABLE if exists hunters;''')

    connection.commit()


def create_tables(connection):
    """Luo tietokantataulut.
    Args:
        connection: Tietokantayhteyden Connection-olio
    """

    cursor = connection.cursor()

    with open('src/data/riddles.sql', mode='r', encoding='utf-8') as riddles_file:
        sql_scrip=riddles_file.read()
    cursor.executescript(sql_scrip)
    with open('src/data/hunters.sql', mode='r', encoding='utf-8') as hunters_file:
        sql_sqript=hunters_file.read()
    cursor.executescript(sql_sqript)
    connection.commit()


def initialize_database():
    """Alustaa tietokantataulut.
    """
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)

if __name__ == "__main__":
    initialize_database()
