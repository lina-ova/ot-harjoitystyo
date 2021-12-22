from initialize_database import initialize_database


def build():

    """Funktio, joka kutsuu toista fuktiota laustakseen tietokannat
    """

    initialize_database()


# This allows us to call the build function using command line
if __name__ == '__main__':
    build()
    