from excel.dto.DtoIterator import Dto


class ForeldriDto(Dto):
    def is_empty(self):
        return not self.__nafn

    __COL_NAFN = "B"
    __COL_THRIFASTADA = "C"
    __COL_HUS = ["D", "E", "F"]

    def __init__(self, nafn, thrifastada, husalisti):
        self.__nafn = nafn
        self.__thrifastada = thrifastada
        self.__husalisti = husalisti #list(filter(lambda v: v, [self.get_value(h) for h in self.__COL_HUS]))

    def get_nafn(self):
        return self.__nafn

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


