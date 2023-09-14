from random import shuffle

from entity.Allocation import Allocation


class Foreldri:
    def __init__(self, nafn, huslisti: [], has_extra_thrif=False, allocations=None):
        if allocations is None:
            allocations = []
        self.__allocations = allocations
        self.__nafn = nafn
        shuffle(huslisti)
        self.__huslisti = huslisti
        self.__has_extra_thrif = has_extra_thrif

    def get_count(self):
        return len(self.__allocations)

    def get_nafn(self):
        return self.__nafn

    def has_extra_thrif(self):
        return self.__has_extra_thrif

    def add_allocation(self, alloc: Allocation):
        self.__allocations += [alloc]

    def get_vikur(self):
        return [a.get_vika() for a in self.__allocations]

    def get_husalisti(self):
        return self.__huslisti

    def get_vikubil(self):
        if len(self.__allocations) == 1:
            return 0

        min_vikubil = 100
        for i in range(1, len(self.__allocations)):
            min_vikubil = min(min_vikubil, abs(self.__allocations[i - 1].get_vika() - self.__allocations[i].get_vika()))
        return min_vikubil

    def __str__(self):
        return "{} = fjoldi: {}, vikubil: {}, vikur: {}".format(self.__nafn, self.get_count(),
                                                                self.get_vikubil(), [v.get_vika() for v in self.__allocations])
