from excel.Column import Column


class ThrifalistiColumn(Column):
    def __init__(self, pos, setter, getter, is_thrif=False):
        super().__init__(pos, setter, getter)
        self.__is_thrif = is_thrif

    def is_thrif(self):
        return self.__is_thrif


class ThrifalistiDto:

    def __init__(self):
        self.__thrifalisti = {}
        self.__vika_texti = None

    def add_to_thrifalisti(self, hus, foreldri):
        self.__thrifalisti[hus] = foreldri

    def get_thrif(self, hus):
        try:
            return self.__thrifalisti[hus]
        except KeyError:
            raise KeyError

    def set_vika_texti(self, vika_texti):
        self.__vika_texti = vika_texti

    def get_vika_texti(self):
        return self.__vika_texti
