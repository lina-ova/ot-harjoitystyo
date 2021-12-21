import unittest
from define.define_result import DefineResult

class TestDefineResult(unittest.TestCase):
    def setUp(self):
        self.result=DefineResult(1100)


    
    def test_define_result_win(self):
        self.result._define_result('win')
        self.assertEqual(self.result._result, 'win')

    def test_define_result_die(self):
        self.result._define_result('die')
        self.assertEqual(self.result._result, 'die')
    
    def test_result_return_write(self):
        self.result._define_result('die')
        self.assertEqual(self.result.result(), 'die')
    
    def test_treasure_change_return_correct(self):
        self.result._define_result('win')
        self.assertEqual(self.result.treasure_change(), self.result._treasure_change)    
    
    def test_balance_return_correct(self):
        self.result._define_result('win')
        self.assertEqual(self.result.balance(),self.result._balance)
    
    def test_lose_treasure_result_treasure_change_correct(self):
        self.result._lose_treasure_result()
        self.assertIsNotNone(self.result._treasure_change)
    
    def test_check_treasure_loss_more_than_balance(self):
        check=self.result._check_treasure_balance(12000)
        self.assertFalse(check)
    
    def test_define_result_lose(self):
        self.result._define_result('lose')

    


        



        
        
