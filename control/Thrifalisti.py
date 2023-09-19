from entity.Foreldri import Foreldri
from entity.Allocation import Allocation
from entity.Vika import Vika


class Thrifalisti:

    def __init__(self, vikulisti, huslisti):
        self.__huslisti = huslisti
        vikulisti.sort(key=lambda v: v.get_vika_nr())
        self.__vikulisti: [Vika] = vikulisti
        self.__vikulisti_no_fri = list(filter(lambda v: not v.is_fri(), vikulisti))

    def get_vikulisti(self):
        return self.__vikulisti_no_fri

    def get_thrifalisti_i_viku(self, vika) -> Vika:
        return self.__vikulisti[vika]

    def get_foreldri(self, vika, hus):
        return self.get_thrifalisti_i_viku(vika).get_foreldri_i_husi(hus)

    def is_all_vika_full(self):
        return all([v.is_full() for v in self.__vikulisti])

    def __str__(self):
        result = "vika,"
        for hus in self.__huslisti:
            result += hus.get_nafn() + ","
        result = result[0: len(result) - 1]
        for v in range(len(self.__vikulisti)):
            result += "\n"
            result += str(v + 1) + ","
            for hus in self.__huslisti:
                result += str(self.get_foreldri(v, hus).get_nafn()) + ","
            result = result[0: len(result) - 1]
        return result
