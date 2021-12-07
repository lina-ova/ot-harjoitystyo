from random import choices, randint

class Result:
    def __init__(self, treasure_balance, change_treasure_value, handle_win, handle_die, handle_lose):
        self._treasure_balance=treasure_balance
        self._change_treasure_value=change_treasure_value
        self._open_win=handle_win
        self._open_die=handle_die
        self._open_lose=handle_lose
        self._determine()

    def _win_result(self):
        win=self._randomise_treasure()
        self._change_treasure_value(win)
        self._open_win(win)
        
    def _die_result(self):
        treasure_lose=-self._treasure_balance
        self._change_treasure_value(treasure_lose)
        self._open_die()

    def _lose_treasure_result(self):
        loss=self._randomise_treasure()
        treasure_balance_check=self._check_treasure_balance(loss)
        if treasure_balance_check:
            self._change_treasure_value(-loss)
            self._open_lose
        else:
            self._die_result

    def _define_result(self, result):
        if result==1:
            self._win_result()
        if result==2:
            self._die_result()
        if result==3:
            self._lose_treasure_result()    

    def _determine(self):

        result=self._randomise_result()
        self._define_result(result)

    def _randomise_result(self):
        results=[1, 2, 3]
        probability=[10,0,3]
        result=choices(results,weights=probability)[0]
        return result

    def _randomise_treasure(self):
        return randint(10,1000)

    def _check_treasure_balance(self,treasure_loss):
        if self._treasure_balance>=treasure_loss:
            return True
        else:
            return False
        


