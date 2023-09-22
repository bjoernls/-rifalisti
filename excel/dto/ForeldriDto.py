

class ForeldriDto:
    def __init__(self):
        self.__nafn = None
        self.__thrifastada = None
        self.__husalisti = []

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
