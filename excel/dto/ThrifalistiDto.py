from excel.dto.DtoIterator import Dto, Column


class ThrifalistiColumn(Column):
    def __init__(self, pos, setter, getter, col_id=None):
        super().__init__(pos, setter, getter)
        self.__id = col_id

    def get_id(self):
        return self.__id

class ThrifalistiDto(Dto):

    def __init__(self):
        self.thrif_rauda = None
        self.thrif_ljosblaa = None
        self.thrif_dokkblaa = None
        self.thrif_graena = None
        self.thrif_tobiasar = None
        self.thrif_skemman = None

        self.columns = [ThrifalistiColumn("A", lambda v: self.set_vika_texti(v), lambda _: self.get_vika_texti())]
        self.columns += [ThrifalistiColumn("B", lambda f: self.set_thrif_rauda(f), lambda: self.get_thrif_rauda(), "Rauða")]
        self.columns += [ThrifalistiColumn("C", lambda f: self.set_thrif_ljosblaa(f), lambda: self.get_thrif_ljosblaa(), "Ljósbláa")]
        self.columns += [ThrifalistiColumn("D", lambda f: self.set_thrif_dokkblaa(f), lambda: self.get_thrif_dokkblaa(), "Dökkbláa")]
        self.columns += [ThrifalistiColumn("E", lambda f: self.set_thrif_graena(f), lambda: self.get_thrif_graena(), "Græna")]
        self.columns += [ThrifalistiColumn("F", lambda f: self.set_thrif_tobiasar(f), lambda: self.get_thrif_tobiasar(), "Tóbíasar")]
        self.columns += [ThrifalistiColumn("G", lambda f: self.set_thrif_skemman(f), lambda: self.get_thrif_skemman(), "Skemman")]

    def get_columns(self):
        return self.columns

    def get_vika_texti(self):
        return self.__vika_texti

    def is_empty(self):
        return not self.__vika_texti or self.__vika_texti == ""

    def skip(self):
        return "haustfrí" in self.__vika_texti

    def set_vika_texti(self, vika_texti):
        self.__vika_texti = vika_texti

    def set_thrif_rauda(self, f):
        self.thrif_rauda = f

    def set_thrif_ljosblaa(self, f):
        self.thrif_ljosblaa = f

    def set_thrif_dokkblaa(self, f):
        self.thrif_dokkblaa = f

    def set_thrif_graena(self, f):
        self.thrif_graena = f

    def set_thrif_tobiasar(self, f):
        self.thrif_tobiasar = f

    def set_thrif_skemman(self, f):
        self.thrif_skemman = f

    def get_thrif_rauda(self):
        return self.thrif_rauda

    def get_thrif_ljosblaa(self):
        return self.thrif_ljosblaa

    def get_thrif_dokkblaa(self):
        return self.thrif_dokkblaa

    def get_thrif_graena(self):
        return self.thrif_graena

    def get_thrif_tobiasar(self):
        return self.thrif_tobiasar

    def get_thrif_skemman(self):
        return self.thrif_skemman
