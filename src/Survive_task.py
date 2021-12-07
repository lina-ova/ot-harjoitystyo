#from database_connection import get_database_connection
import random

class SurviveTask:
    def __init__(self, connection, handle_survive_view):
        self._connection=connection
        self._open_survive_view=handle_survive_view
        self._get_task()
    def randomize_task(self):
        task_id=random.randint(1,15)
        return str(task_id)

    def _get_from_database(self, task_id):
        
        cursor=self._connection.cursor()
        task_and_answer=cursor.execute('SELECT riddle, answer FROM riddles WHERE id=?', [task_id]).fetchone()
        return task_and_answer

    def _get_task(self):
        task_id=self.randomize_task()
        task_and_answer=self._get_from_database(task_id)
        riddle=task_and_answer[0]
        answer=task_and_answer[1]
        self._handle_survive_view(riddle, answer)

    def _handle_survive_view(self, riddle, answer):
        pass
        self._open_survive_view(riddle, answer)

