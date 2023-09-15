from random import randint


class Hus:

    def __init__(self, nafn, vikufjoldi, exklusift=False):
        self.__exklusift = exklusift
        self.__nafn = nafn
        self.__vikur = [v for v in range(vikufjoldi)]

    def is_full(self):
        return len(self.__vikur) == 0

    def get_nafn(self):
        return self.__nafn

    def remove_vika(self, vika):
        self.__vikur.remove(vika)

    def get_vika(self):
        return self.__vikur[randint(len(self.__vikur) - 1)]

    def is_exclusift(self):
        return self.__exklusift

    def get_vikur(self):
        return self.__vikur

    def __str__(self):
        return self.__nafn + ": " + str(self.__vikur)
