from matchers import *

class QueryBuilder:
    def __init__(self, all=All()):
        self._all = all

    def build(self):
        return self._all
    
    def playsIn(self, team):
        return QueryBuilder(And(PlaysIn(team), self._all))
    
    def hasAtLeast(self, value, attribute):
        return QueryBuilder(And(HasAtLeast(value, attribute), self._all))
        
    def hasFewerThan(self, value, attribute):
        return QueryBuilder(And(HasFewerThan(value, attribute), self._all))
