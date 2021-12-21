import unittest
from database_connection import get_database_connection
from define.survivetask import SurviveTask

class TestSurviveTask(unittest.TestCase):
    def setUp(self):
        self.task=SurviveTask()
    
    def test_connection_exists(self):
        self.assertIsNotNone(self.task._connection)
    
    def test_riddle_return(self):
        self.assertEqual(self.task.riddle(), self.task._riddle)
    
    def test_answer_return(self):
        self.assertEqual(self.task.answer(), self.task._answer)
    
    def test_check_user_answer_return_survive(self):
            correct='vastaus'
            users='vastaus'
            check=self.task.check_user_answer(correct, users)
            self.assertEqual(check, 'survive')
    
    def test_check_user_answer_return_digest(self):
            correct='vastaus'
            users='answer'
            check=self.task.check_user_answer(correct, users)
            self.assertEqual(check, 'digest')
    