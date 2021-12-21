import random
from database_connection import get_database_connection

class SurviveTask:
    """Luokka joka vastaa:
        pelaajalle suoritettavaksi annettavan tehtävän hakemisesta tietokannasta"""
    def __init__(self):
        """Connection: Tietokantayhteyden Connection-olio
            riddle: tehtävänanto
            answer: oikea vastatus
            """
        self._connection=get_database_connection()
        self._riddle=None
        self._answer=None
        self._get_task()
    def randomize_task(self):
        """Funktio valitsee satunnaisen tehtävänumeron 
            Returns:
                palauttaa tehtävänumeron tekstimuodossa"""
        task_id=random.randint(1,54)
        return str(task_id)

    def _get_from_database(self, task_id):
        """Funktio hakee tehtävänannon ja tehtävävastauksen tietokannasta tehtävänumeron perusteella
            Args:
                tehtävänumero tekstimuodossa
            Returns:
                Tuple(Tehtävä TEXT, vastaus TEXT)"""
        cursor=self._connection.cursor()
        task=cursor.execute('SELECT riddle, answer FROM riddles WHERE id=?', [task_id]).fetchone()
        return task

    def _get_task(self):
        """Funktio määrittää tehtävänannon ja vastauksen
        task_id=kutsuu funktiota, joka palauttaa satunnaisen tehtävänumeron text muodossa
        task_and_answer: kutsuu funktiota, joka palautta Tuplena tehtävänannon ja vastauksen tehtävänumeron perusteella tietokannasta
        riddle: luokan argumentti tehtävänannolle
        answer: luokkaargumentti vastaukselle"""
        task_id=self.randomize_task()
        task_and_answer=self._get_from_database(task_id)
        self._riddle=task_and_answer[0]
        self._answer=task_and_answer[1]

    def riddle(self):
        """Funktio:
            Returns: 
                tehtävänanto"""
        return self._riddle

    def answer(self):
        """Funktio 
        Returns:
            tehtävänvastaus"""
        return self._answer

    def check_user_answer(self,correct, users):
        if users==correct:
            return 'survive'
        return 'digest'
