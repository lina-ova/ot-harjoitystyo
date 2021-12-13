from database_connection import get_database_connection

class Hunters:
    def __init__(self):
        self._connection=get_database_connection()
        
    def get_from_history(self):
        cursor=self._connection.cursor()
        best_hunters=cursor.execute('SELECT * FROM hunters ORDER BY treasures DESC').fetchall()
        return best_hunters
    def get_three_best_from_history(self):
        cursor=self._connection.cursor()
        best_hunters=cursor.execute('SELECT * FROM hunters ORDER BY treasures DESC LIMIT 3').fetchall()
        _return_ = []
        for hunter in best_hunters:
            name=hunter[0]
            treasures=str(hunter[1])
            status=hunter[2]
            _return_.append('Name: '+name+' Treasures: '+treasures+' status: '+status)
        return _return_
    def check_name_unique(self, name):
        hunters=self.get_from_history()
        
        for hunter in hunters:
            if hunter[0]==name:

                return False
        return True

    def write_to_history(self, name, treasures, alive):
        cursor=self._connection.cursor()
        cursor.execute('INSERT INTO hunters(name, treasures, alive) VALUES(?,?,?)',[name, treasures, alive])
        self._connection.commit()
    def get_hunter(self, name):
        unique_name=self.check_name_unique(name)
        if not unique_name:
            cursor=self._connection.cursor()
            search_result=cursor.execute('SELECT * FROM(SELECT name, treasures,alive, RANK() OVER (ORDER BY treasures DESC) FROM hunters) WHERE name=?',[name]).fetchone()
            name=search_result[0]
            treasures=str(search_result[1])
            status=search_result[2]
            rank=str(search_result[3])
            _return_='Name:'+name+'\nTreasures: '+treasures+'\nStatus: '+'\n Rank: '+rank
            return _return_
        else:
            return 'not such hunter in history'



