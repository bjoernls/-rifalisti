from excel.Column import convert_to_num


def get_sheet_value(sheet, col, row):
    return sheet.cell(row, convert_to_num(col)).value


class SheetReader:

    def __init__(self, sheet, info, columns, dto_factory):
        self._sheet = sheet
        self._info = info
        self._columns = columns
        self._dto_factory = dto_factory

    def _create_dtos(self):
        dtos = []

        columns = self._columns
        row = self._info.get_start_read_row_col()[0]

        while not self.__is_row_empty(row, columns):
            dto = self._dto_factory()
            for col in columns:
                val = self.get_sheet_value(row, col.get_pos())
                self._set_dto_value(col, dto, val)
            row += 1
            dtos += [dto]

        return dtos

    def _set_dto_value(self, col, dto, val):
        col.setter(dto, val)

    def __is_row_empty(self, row, columns):
        return all([self.get_sheet_value(row, col.get_pos()) is None for col in columns])

    def read(self):
        return self._create_dtos()

    def get_sheet_value(self, row, col):
        return get_sheet_value(self._sheet, col, row)


class ThrifalistiSheetReader(SheetReader):

    def __init__(self, sheet, info, columns, dto_factory, col_to_hus_map):
        super().__init__(sheet, info, columns, dto_factory)
        self.__col_to_hus_map = col_to_hus_map

    def _set_dto_value(self, col, dto, val):
        if col.is_thrif():
            col.setter(dto, self.__col_to_hus_map[col.get_pos()], val)
        else:
            col.setter(dto, val)
