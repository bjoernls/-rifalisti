from excel.dto.DtoIterator import Dto


class ThrifalistiDto(Dto):

    def __init__(self, vika_texti):
        self.__vika_texti = vika_texti

    def is_empty(self):
        return not self.__vika_texti or self.__vika_texti == ""

    def skip(self):
        return "haustfrí" in self.__vika_texti
