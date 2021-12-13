from database_connection import get_database_connection
import random

class SurviveTask:
    def __init__(self):
        self._connection=get_database_connection()
        self._riddle=None
        self._answer=None
        self._get_task()
    def randomize_task(self):
        task_id=random.randint(1,54)
        return str(task_id)

    def _get_from_database(self, task_id):
        
        cursor=self._connection.cursor()
        task_and_answer=cursor.execute('SELECT riddle, answer FROM riddles WHERE id=?', [task_id]).fetchone()
        return task_and_answer

    def _get_task(self):
        task_id=self.randomize_task()
        task_and_answer=self._get_from_database(task_id)
        self._riddle=task_and_answer[0]
        self._answer=task_and_answer[1]

    def riddle(self):
        return self._riddle
    
    def answer(self):
        return self._answer

