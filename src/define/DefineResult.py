
from random import choices, randint

class DefineResult:
    def __init__(self, treasure):
        self._balance=treasure
        self._treasure_change=None
        self._result=None
        self._determine()


    def _determine(self):

        result=self._randomise_result()
        self._define_result(result)

    def _randomise_result(self):
        results=['win', 'die', 'lose']
        probability=[5,4,3]
        result=choices(results,weights=probability)[0]
        return result
    
    def _define_result(self, result):
        if result=='win':
            self._win_result()
        if result=='die':
            self._die_result()
        if result=='lose':
            self._lose_treasure_result()


    def _set_result(self, result):
        self._result=result

    def result(self):
        return self._result

    def treasure_change(self):
        return self._treasure_change

    def balance(self):
        return self._balance

    def _win_result(self):
        self._set_result('win')

        self._treasure_change=self._randomise_treasure()

        self._balance+=self._treasure_change
        
    
    def _die_result(self):
        
        self._set_result('die')

    def _lose_treasure_result(self):
        loss=self._randomise_treasure()
        treasure_balance_check=self._check_treasure_balance(loss)
        if treasure_balance_check:
            self._treasure_change=-loss
            self._balance+=self._treasure_change
            self._set_result('lose')
        else:
            self._die_result()
    
    def _randomise_treasure(self):
        return randint(10,1000)

    def _check_treasure_balance(self,loss):
    
        if self._balance>loss:
            return True
        else:
            return False
    
