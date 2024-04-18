class Allocation:
    def __init__(self, vika, hus):
        self.__hus = hus
        self.__vika = vika

    def get_vika(self):
        return self.__vika.get_nr()

    def get_vika_texti(self):
        return self.__vika.get_texti()

    def get_hus(self):
        return self.__hus
