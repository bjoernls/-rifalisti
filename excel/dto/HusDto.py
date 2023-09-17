from excel.dto.DtoIterator import Dto


class HusDto(Dto):
    def is_empty(self):
        return self.__nafn is None

    __COL_NAFN = "A"
    __COL_EXCLUSIVE = "B"

    def __init__(self, nafn, is_exclusive):
        self.__nafn = nafn
        self.__is_exclusive = is_exclusive

    def get_nafn(self):
        return self.__nafn

    def is_exclusive(self):
        return self.__is_exclusive

    def __str__(self):
        return f'nafn: {self.__nafn}, exlusive: {self.__exclusive}'
