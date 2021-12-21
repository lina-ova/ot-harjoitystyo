import unittest
from define.best_hunters import Hunters
from build import build

class TestHunters(unittest.TestCase):
    def setUp(self):
        build()
        self.name_unique='Janne Laukku'
        self._name_not_unique='Jon Tuska'
        self.treasures=1000
        self.status='alive'
        self.hunters=Hunters()
    
    def test_return_from_history_list(self):
        hunters=self.hunters.get_from_history()
        self.assertIsNotNone(hunters)
    
    def test_get_three_correct(self):
        hunters=self.hunters.get_three_best_from_history()
        self.assertIsNotNone(hunters)
    
    def test_check_name_unique(self):

        check=self.hunters.check_name_unique(self.name_unique)
        self.assertTrue(check)
    
    def test_check_name_not_unique(self):
        check=self.hunters.check_name_unique(self._name_not_unique)
        self.assertFalse(check)
    
    def test_write_to_history_name_in_database(self):
        
        self.hunters.write_to_history(self.name_unique, self.treasures, self.status)
        check=self.hunters.check_name_unique(self.name_unique)
        self.assertFalse(check)
    
    def test_get_hunter_from_database_hunter_exist(self):
        search=self.hunters.get_hunter(self._name_not_unique)
        incorrect_search='not such hunter in history'

        self.assertNotEqual(search, incorrect_search)
    
    def test_get_hunter_from_database_hunter_not_exist(self):
        search=self.hunters.get_hunter('jhghjkgk')
        incorrect_search='not such hunter in history'
        self.assertEqual(search, incorrect_search)
        

    
    
        