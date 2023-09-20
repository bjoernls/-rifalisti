from excel.dto.DtoIterator import DtoIterator
from excel.sheet_infos.ForeldriSheetInfo import ForeldriSheetInfo
from excel.sheet_infos.HusSheetInfo import HusSheetInfo
from excel.sheet_infos.SheetInfo import SheetInfo
from excel.sheet_infos.ThrifalistiSheetInfo import ThrifalistiSheetInfo
from mapper.Mapper import Mapper, HusMapper, ForeldriMapper, ThrifalistiMapper


def filter_cols_before_start(column, info):
    return ord(column.get_pos()) >= ord(info.get_start_write_row_col()[1])


class SheetHandler:

    def __init__(self, wb, info):
        self.__sheet = wb[info.get_sheet_name()]
        self.__info: SheetInfo = info

    def get_sheet(self):
        return self.__sheet

    def get_mapper(self):
        raise NotImplementedError

    def read(self):
        mapper = self.get_mapper()
        return [mapper.map_to_entity(dto) for dto in DtoIterator(self.__sheet, self.__info)]

    def write(self, entities):
        row_no = self.__info.get_start_write_row_col()[0]
        for dto in self.create_dtos(entities):
            filtered_cols = list(filter(lambda c: filter_cols_before_start(c, self.__info), dto.get_columns()))
            for col in filtered_cols:
                self.__sheet.cell(row_no, col.get_pos_num()).value = col.getter()
            row_no += 1

    def create_dtos(self, entities):
        raise NotImplementedError


class HusSheetHandler(SheetHandler):
    def __init__(self, wb):
        super().__init__(wb, HusSheetInfo())

    def get_mapper(self):
        return HusMapper()


class ForeldriSheetHandler(SheetHandler):
    def __init__(self, wb, husalisti):
        super().__init__(wb, ForeldriSheetInfo())
        self.__husalisti = husalisti

    def get_mapper(self):
        return ForeldriMapper(self.__husalisti)


class ThrifalistiSheetHandler(SheetHandler):
    def __init__(self, wb, husalisti):
        super().__init__(wb, ThrifalistiSheetInfo())
        self.__husalisti = husalisti

    def get_mapper(self):
        return ThrifalistiMapper(self.__husalisti)

    def create_dtos(self, thrifalisti):
        dtos = [self.get_mapper().map_to_dto(thrifalisti.get_vikuthrifalisti(v.get_vika_nr())) for v in
                thrifalisti.get_vikuthrifalistar()]
        return dtos
