from math import ceil, floor

from entity.Allocation import Allocation
from entity.Foreldri import Foreldri
from linked_list.LeveledLinkedLists import LeveledLinkedLists
from control.Thrifalisti import Thrifalisti


def get_min_vikubil(vika, vikur):
    return min([abs(v - vika.get_vika_nr()) for v in vikur])


class ThrifalistiAlgo:

    def __init__(self, huslisti, viku_fjoldi, foreldralisti: [Foreldri]):
        self.__min_vikubil = floor(viku_fjoldi / 2)
        self.viku_fjoldi = viku_fjoldi
        self.__huslisti = huslisti
        self.__leveled_linked_lists = LeveledLinkedLists(foreldralisti,
                                                         self.__calc_max_level(foreldralisti, huslisti, viku_fjoldi))

    def __calc_max_level(self, foreldralisti, huslisti, viku_fjoldi):
        return ceil(float(len(huslisti) * viku_fjoldi) / len(foreldralisti)) + 1

    def compute(self, thrifalisti: Thrifalisti):
        while not thrifalisti.is_all_vika_full():
            if self.__is_deadlock():
                self.__resolve_deadlock(thrifalisti)
            foreldri = self.__leveled_linked_lists.pop()

            alloc_found = self.__find_alloc(foreldri, thrifalisti)

            if not alloc_found:
                self.__leveled_linked_lists.retry()
                continue
            elif foreldri.has_less_thrif():
                self.__leveled_linked_lists.discard()
            else:
                self.__leveled_linked_lists.commit()

    def __find_alloc(self, foreldri, thrifalisti):
        for vika in self.__get_vikur_ekki_of_nalaegt(thrifalisti, foreldri):
            if vika.try_set_foreldri(foreldri):
                return True
        return False

    def __get_vikur_ekki_of_nalaegt(self, thrifalisti, foreldri):
        return list(filter(lambda vika: not self.is_of_nalaegt(foreldri.get_vikur(), vika),
                           thrifalisti.get_vikulisti()))

    def is_of_nalaegt(self, foreldri_vikur, vika):
        if len(foreldri_vikur) == 0:
            return False
        return any([abs(v - vika.get_vika_nr()) < self.__min_vikubil for v in foreldri_vikur])

    def __is_deadlock(self):
        return self.__leveled_linked_lists.is_deadlock()

    def __resolve_deadlock(self, thrifalisti):
        retry_pile = self.__get_retry_pile().copy()

        avail_vikur = list(filter(lambda v: not v.is_full(), thrifalisti.get_vikulisti()))

        for vika in avail_vikur:
            f = self.__set_foreldri_with_max_vikubil(retry_pile, vika)
            if not f:
                continue
            retry_pile.remove(f)
            if len(retry_pile) == 0:
                break

        self.__leveled_linked_lists.reset_deadlock()

    def __get_retry_pile(self):
        return self.__leveled_linked_lists.get_retry_pile()

    def __set_foreldri_with_max_vikubil(self, retry_pile, vika):
        retry_pile.sort(key=lambda f: get_min_vikubil(vika, f.get_vikur()), reverse=True)
        for f in retry_pile:
            if vika.try_set_foreldri(f):
                return f
        return None