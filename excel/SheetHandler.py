from excel.dto.DtoIterator import DtoIterator
from excel.sheet_infos.SheetInfo import SheetInfo
from mapper.Mapper import Mapper


def filter_cols_before_start(column, info):
    return ord(column.get_pos()) >= ord(info.get_start_write_row_col()[1])


class SheetHandler:

    def __init__(self, wb, info):
        self.__sheet = wb[info.get_sheet_name()]
        self.__info: SheetInfo = info

    def get_sheet(self):
        return self.__sheet

    def read(self, mapper: Mapper):
        return [mapper.map_to_entity(dto) for dto in DtoIterator(self.__sheet, self.__info)]

    def write(self, dtos):
        row_no = self.__info.get_start_write_row_col()[0]
        for dto in dtos:
            filtered_cols = list(filter(lambda c: filter_cols_before_start(c, self.__info), dto.get_columns()))
            for col in filtered_cols:
                self.__sheet.cell(row_no, col.get_pos_num()).value = col.getter()
            row_no += 1
