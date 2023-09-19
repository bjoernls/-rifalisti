from entity.Allocation import Allocation


class VikuThrifalisti:
    def __init__(self, vika_nr, vika_texti, is_fri, thrifalisti_fyrir_viku, non_exclusive_husalisti):
        self.__thrifalisti_fyrir_viku = thrifalisti_fyrir_viku
        self.__vika_nr = vika_nr
        self.vika_texti = vika_texti
        self.__is_fri = is_fri
        self.__non_exclusive_husalisti = non_exclusive_husalisti

    def __sub__(self, other):
        return self.__vika_nr - other.get_vika_nr()

    def is_fri(self):
        return self.__is_fri

    def get_vika_nr(self):
        return self.__vika_nr

    def get_foreldri_i_husi(self, hus):
        return self.__thrifalisti_fyrir_viku[hus]

    def set_foreldri_i_husi(self, hus, foreldri):
        foreldri.add_allocation(Allocation(self.__vika_nr, hus))
        self.__thrifalisti_fyrir_viku[hus] = foreldri

    def try_set_foreldri(self, foreldri):
        for hus in foreldri.get_husalisti():
            if not self.__thrifalisti_fyrir_viku[hus]:
                self.set_foreldri_i_husi(hus, foreldri)
                return hus

        for hus in self.__non_exclusive_husalisti:
            if not self.__thrifalisti_fyrir_viku[hus]:
                self.set_foreldri_i_husi(hus, foreldri)
                return hus

        return None

    def is_full(self):
        return self.is_fri() or all([f for f in self.__thrifalisti_fyrir_viku.values()])
