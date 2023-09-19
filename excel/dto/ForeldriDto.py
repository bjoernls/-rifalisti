from excel.dto.DtoIterator import Dto, Column


class ForeldriDto(Dto):
    def is_empty(self):
        return not self.__nafn

    def __init__(self):
        self.__nafn = None
        self.__thrifastada = None
        self.__husalisti = []

        self.columns = [Column("B", lambda nafn: self.set_nafn(nafn), lambda: self.get_nafn())]
        self.columns += [Column("C", lambda ts: self.set_thrifastada(ts), lambda: self.get_thrifastada())]
        self.columns += [Column("D", lambda hus: self.add_hus(hus), lambda: self.get_husalisti())]
        self.columns += [Column("E", lambda hus: self.add_hus(hus), lambda: self.get_husalisti())]
        self.columns += [Column("F", lambda hus: self.add_hus(hus), lambda: self.get_husalisti())]

    def get_columns(self):
        return self.columns

    def add_hus(self, hus):
        if hus:
            self.__husalisti += [hus]

    def set_nafn(self, nafn):
        self.__nafn = nafn

    def get_nafn(self):
        return self.__nafn

    def set_thrifastada(self, ts):
        self.__thrifastada = ts

    def get_thrifastada(self):
        return self.__thrifastada

    def has_less_thrif(self):
        return self.__thrifastada == 1

    def has_auka_thrif(self):
        return self.__thrifastada == -1

    def get_husalisti(self):
        return self.__husalisti

    def __str__(self):
        return f'nafn: {self.__nafn}, þrifastaða: {self.__thrifastada}, husalisti: {self.__husalisti}'


# mappar Dto yfir í Foreldri-object
class ForeldriDtoMapper:
    def __init__(self, huslisti):
        self.huslisti = huslisti

    def map(self, dto: ForeldriDto):
        pass
