FRI = ["Vetrarfrí", "Páskafrí", "Sumarfrí"]


class Vika:

    def __init__(self, vika_nr, texti):
        self.__texti = texti
        self.__vika_nr = vika_nr

    def is_fri(self):
        return any(fri in self.__texti for fri in FRI)

    def get_texti(self):
        return self.__texti

    def get_nr(self):
        return self.__vika_nr