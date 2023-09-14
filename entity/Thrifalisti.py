from entity.Foreldri import Foreldri
from entity.Allocation import Allocation


class Thrifalisti:
    __EMPTY_DATA = Foreldri("", [])

    def __init__(self, viku_fjoldi, huslisti):
        self.__huslisti = huslisti
        self.__viku_fjoldi = viku_fjoldi
        self.__init_thrifalisti()

    def __init_thrifalisti(self):
        self.__thrifalisti = []
        for v in range(self.__viku_fjoldi):
            self.__thrifalisti += [{}]
            for hus in self.__huslisti:
                self.__thrifalisti[v][hus] = self.__EMPTY_DATA

    def get_foreldri(self, vika, hus):
        return self.__thrifalisti[vika][hus]

    def is_empty(self, vika, hus):
        return self.get_foreldri(vika, hus) == self.__EMPTY_DATA

    def set_foreldri(self, allocation: Allocation, foreldri):
        vika = allocation.get_vika()
        hus = allocation.get_hus()

        if self.__thrifalisti[vika][hus] is not self.__EMPTY_DATA:
            raise RuntimeError("Villa")
        self.__thrifalisti[vika][hus] = foreldri

        foreldri.add_allocation(allocation)
        hus.remove_vika(vika)

    def is_foreldri_i_viku(self, vika, foreldri):
        for hus in self.__thrifalisti[vika]:
            if foreldri == self.__thrifalisti[vika][hus]:
                return True
        return False

    def is_all_hus_full(self):
        for hus in self.__huslisti:
            if hus.is_available():
                return False
        return True

    def __str__(self):
        result = "vika,"
        for hus in self.__huslisti:
            result += hus.get_nafn() + ","
        result = result[0: len(result) - 1]
        for v in range(self.__viku_fjoldi):
            result += "\n"
            result += str(v + 1) + ","
            for hus in self.__huslisti:
                result += str(self.__thrifalisti[v][hus].get_nafn()) + ","
            result = result[0: len(result) - 1]
        return result

    def is_slot_available(self, vika, hus):
        return self.get_foreldri(vika, hus) is self.__EMPTY_DATA