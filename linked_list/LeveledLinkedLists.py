from entity.Foreldri import Foreldri
from entity.Strategy import RandomStrategy
from linked_list.LinkedList import LinkedList


class LeveledLinkedLists:

    def __init__(self, foreldralisti: [Foreldri], max_level):
        self.__init_linked_lists(foreldralisti, max_level)
        self.level = 0
        self.curr_lllist: LinkedList = self.all_llls[self.level]
        self.tmp_foreldri = None
        self.__reset_pile = []
        self.__deadlock = False

    def __init_linked_lists(self, foreldralisti: [Foreldri], max_level):
        self.all_llls = []
        for _ in range(0, max_level + 5):
            self.all_llls += [LinkedList([], RandomStrategy())]

        for f in foreldralisti:
            self.all_llls[f.get_count()].push(f)

    def pop(self):
        self.tmp_foreldri = self.curr_lllist.pop_strategy()

        if self.curr_lllist.is_empty():
            if self.__reset_pile:
                self.__deadlock = True
            self.__increase_level()

        return self.tmp_foreldri

    def __increase_level(self):
        self.level += 1
        self.curr_lllist = self.all_llls[self.level]

    def discard(self):
        self.tmp_foreldri = None

    def commit(self):
        self.all_llls[self.level + 1].push(self.tmp_foreldri)
        self.tmp_foreldri = None

    def reset(self):
        self.__reset_pile += [self.tmp_foreldri]
        self.tmp_foreldri = None

    def is_deadlock(self):
        return self.__deadlock

    def reset_deadlock(self):
        self.__deadlock = False
        for f in self.__reset_pile:
            self.curr_lllist.push(f)

    def get_reset_pile(self):
        return self.__reset_pile
