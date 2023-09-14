from math import ceil, floor

from entity.Allocation import Allocation
from entity.Foreldri import Foreldri
from linked_list.LeveledLinkedLists import LeveledLinkedLists
from entity.Thrifalisti import Thrifalisti


class ThrifalistiAlgo:

    def __init__(self, huslisti, viku_fjoldi, foreldralisti: [Foreldri]):
        self.__min_vikubil = floor(viku_fjoldi / 2)
        self.__foreldri_i_excl_husum = {}
        self.viku_fjoldi = viku_fjoldi
        self.__huslisti = huslisti
        self.__thrifalisti = Thrifalisti(viku_fjoldi, huslisti)
        self.__leveled_linked_lists = LeveledLinkedLists(foreldralisti,
                                                         self.__calc_max_level(foreldralisti, huslisti, viku_fjoldi))

    def __calc_max_level(self, foreldralisti, huslisti, viku_fjoldi):
        return ceil(float(len(huslisti) * viku_fjoldi) / len(foreldralisti)) + 1

    def get_thrifalisti(self):
        return self.__thrifalisti

    def compute(self):
        while not self.__thrifalisti.is_all_hus_full():
            if self.__is_deadlock():
                self.__resolve_deadlock()
            foreldri = self.__leveled_linked_lists.pop()
            alloc = self.__find_avail_alloc(foreldri)

            if alloc is None:
                self.__leveled_linked_lists.reset()
                continue
            elif foreldri.has_extra_thrif():
                self.__leveled_linked_lists.discard()
            else:
                self.__leveled_linked_lists.commit()
            self.__thrifalisti.set_foreldri(alloc, foreldri)

    def __find_avail_alloc(self, foreldri):
        alloc = self.__find_avail_hus_in_list(foreldri.get_husalisti(), foreldri)

        if alloc is None:
            return self.__find_avail_hus_in_list(self.__get_all_available_non_exclusive_hus(), foreldri)

        return alloc

    def __get_all_available_non_exclusive_hus(self):
        return list(filter(lambda h: not h.is_exclusift(), self.__get_all_available_hus(self.__huslisti)))

    def __get_all_available_hus(self, huslisti):
        return list(filter(lambda h: h.is_available(), huslisti))

    def __find_avail_hus_in_list(self, huslisti, foreldri: Foreldri):
        for hus in self.__get_all_available_hus(huslisti):
            for vika in hus.get_vikur():
                if foreldri.get_count() > 0 and self.is_of_nalaegt(foreldri.get_vikur(), vika):
                    continue
                return Allocation(vika, hus)
        return None

    def is_of_nalaegt(self, vikur, vika):
        return any([abs(v - vika) < self.__min_vikubil for v in vikur])

    def __is_deadlock(self):
        return self.__leveled_linked_lists.is_deadlock()

    def __resolve_deadlock(self):
        reset_pile = self.__get_reset_pile().copy()
        for hus in self.__get_all_available_hus(self.__huslisti):
            for vika in hus.get_vikur().copy():
                max_vikubil_foreldri = self.__get_foreldri_with_max_vikubil(reset_pile, vika, hus)
                if not max_vikubil_foreldri:
                    continue
                self.get_thrifalisti().set_foreldri(Allocation(vika, hus), max_vikubil_foreldri)
                reset_pile.remove(max_vikubil_foreldri)
                if len(reset_pile) == 0:
                    break

        self.__leveled_linked_lists.reset_deadlock()

    def __get_reset_pile(self):
        return self.__leveled_linked_lists.get_reset_pile()

    def __get_foreldri_with_max_vikubil(self, reset_pile, vika, hus):
        rp_list_filtered = list(filter(lambda f: hus in f.get_husalisti(), reset_pile))
        if len(rp_list_filtered) == 0:
            return None
        rp_list_filtered.sort(key=lambda f: self.__get_min_vikubil(vika, f.get_vikur()), reverse=True)
        return rp_list_filtered[0]

    def __get_min_vikubil(self, vika, vikur):
        return min([abs(v - vika) for v in vikur])
