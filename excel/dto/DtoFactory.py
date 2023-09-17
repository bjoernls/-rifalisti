from excel.dto.ForeldriDto import ForeldriDto
from excel.dto.HusDto import HusDto
from excel.dto.ThrifalistiDto import ThrifalistiDto


class DtoFactory:
    def __init__(self, sheet):
        self.sheet = sheet

    @staticmethod
    def __convert_to_num(col):
        return ord(col.lower()) - 96

    def create_dto(self, row):
        raise NotImplementedError

    def get_value(self, row, col):
        return self.sheet.cell(row, self.__convert_to_num(col)).value


class HusDtoFactory(DtoFactory):
    __COL_NAFN = "A"
    __COL_EXCLUSIVE = "B"

    def __init__(self, sheet):
        super().__init__(sheet)

    def create_dto(self, row):
        return HusDto(self.__get_nafn(row), self.__is_exclusive(row))

    def __get_nafn(self, row):
        return self.get_value(row, self.__COL_NAFN)

    def __is_exclusive(self, row):
        return self.get_value(row, self.__COL_EXCLUSIVE)


class ForeldriDtoFactory(DtoFactory):
    __COL_NAFN = "B"
    __COL_THRIFASTADA = "C"
    __COL_HUS = ["D", "E", "F"]

    def __init__(self, sheet):
        super().__init__(sheet)

    def create_dto(self, row):
        return ForeldriDto(self.__get_nafn(row), self.__get_thrifastada(row), self.__get_husalisti(row))

    def __get_nafn(self, row):
        return self.get_value(row, self.__COL_NAFN)

    def __get_thrifastada(self, row):
        return self.get_value(row, self.__COL_THRIFASTADA)

    def __get_husalisti(self, row):
        return list(filter(lambda v: v, [self.get_value(row, col) for col in self.__COL_HUS]))


class ThrifalistiDtoFactory(DtoFactory):

    def __init__(self, sheet):
        super().__init__(sheet)

    def create_dto(self, row):
        dto = ThrifalistiDto()
        for col in dto.get_columns():
            col.setter(self.get_value(row, col.get_pos()))
        return dto

