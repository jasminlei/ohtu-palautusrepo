from matchers import All, And, HasAtLeast, HasFewerThan, PlaysIn, Or


class QueryBuilder:
    def __init__(self):
        self._matcher = All()

    def plays_in(self, team):
        self._matcher = And(self._matcher, PlaysIn(team))
        return self

    def has_at_least(self, value, attr):
        self._matcher = And(self._matcher, HasAtLeast(value, attr))
        return self

    def has_fewer_than(self, value, attr):
        self._matcher = And(self._matcher, HasFewerThan(value, attr))
        return self

    def one_of(self, *matchers):
        self._matcher = Or(*matchers)
        return self

    def build(self):
        matcher = self._matcher
        self._matcher = All()
        return matcher
