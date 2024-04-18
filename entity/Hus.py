class Hus:

    def __init__(self, nafn, exklusift=False):
        self.__exklusift = exklusift
        self.__nafn = nafn

    def get_nafn(self):
        return self.__nafn

    def is_exclusift(self):
        return self.__exklusift

    def __str__(self):
        return self.__nafn + ": "
