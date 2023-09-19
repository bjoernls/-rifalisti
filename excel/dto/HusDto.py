from excel.dto.DtoIterator import Dto, Column


class HusDto(Dto):
    def is_empty(self):
        return self.__nafn is None

    def __init__(self):
        self.__nafn = None
        self.__is_exclusive = False

        self.__columns = [Column("A", lambda nafn: self.set_nafn(nafn), lambda: self.get_nafn())]
        self.__columns += [Column("B", lambda e: self.set_exclusive(e), lambda: self.is_exclusive())]

    def set_nafn(self, nafn):
        self.__nafn = nafn

    def get_nafn(self):
        return self.__nafn

    def get_columns(self):
        return self.__columns

    def is_exclusive(self):
        return self.__is_exclusive

    def set_exclusive(self, is_exclusive):
        if is_exclusive is None:
            return
        self.__is_exclusive = is_exclusive

    def __str__(self):
        return f'nafn: {self.__nafn}, exlusive: {self.__exclusive}'
