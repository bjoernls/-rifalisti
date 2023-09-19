from excel.dto.ForeldriDto import ForeldriDto
from excel.dto.HusDto import HusDto
from excel.dto.ThrifalistiDto import ThrifalistiDto


class DtoFactory:
    def __init__(self, sheet, factory_method):
        self.sheet = sheet
        self.__factory_method = factory_method

    @staticmethod
    def __convert_to_num(col):
        return ord(col.lower()) - 96

    def create_dto(self, row):
        dto = self.__factory_method()
        for col in dto.get_columns():
            col.setter(self.get_value(row, col.get_pos()))
        return dto

    def get_value(self, row, col):
        return self.sheet.cell(row, self.__convert_to_num(col)).value


class HusDtoFactory(DtoFactory):
    def __init__(self, sheet):
        super().__init__(sheet, lambda: HusDto())


class ForeldriDtoFactory(DtoFactory):
    def __init__(self, sheet):
        super().__init__(sheet, lambda: ForeldriDto())


class ThrifalistiDtoFactory(DtoFactory):
    def __init__(self, sheet):
        super().__init__(sheet, lambda: ThrifalistiDto())
