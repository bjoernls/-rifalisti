from excel.dto.Column import convert_to_num
from excel.dto.ForeldriDto import ForeldriDto
from excel.dto.HusDto import HusDto
from excel.dto.ThrifalistiDto import ThrifalistiDto
from excel.sheet_infos.ForeldriSheetInfo import ForeldriSheetInfo
from excel.sheet_infos.HusSheetInfo import HusSheetInfo
from excel.sheet_infos.ThrifalistiSheetInfo import ThrifalistiSheetInfo
from mapper.Mapper import HusMapper, ForeldriMapper, ThrifalistiMapper


def filter_cols_before_start(column, info):
    return ord(column.get_pos()) >= ord(info.get_start_write_row_col()[1])


class SheetHandler:

    @staticmethod
    def __convert_to_num(col):
        return ord(col.lower()) - 96

    def __init__(self, wb, mapper, info):
        self._sheet = wb[info.get_sheet_name()]
        self._mapper = mapper
        self._info = info

    def read(self):
        self._mapper.reset()
        return [self._mapper.map_to_entity(dto) for dto in self.create_dtos()]

    def get_value(self, row, col):
        return self._sheet.cell(row, convert_to_num(col)).value

    def create_dtos(self):
        dtos = []

        columns = self._mapper.get_columns()
        row = self._info.get_start_read_row_col()[0]

        while not self.__is_row_empty(row, columns):
            dto = self._create_dto()
            for col in columns:
                val = self.get_value(row, col.get_pos())
                self._set_value(dto, col, val)
            row += 1
            dtos += [dto]

        return dtos

    def _set_value(self, dto, col, val):
        col.setter(dto, val)

    def _create_dto(self):
        raise NotImplementedError

    def __is_row_empty(self, row, columns):
        return all([self.get_value(row, col.get_pos()) is None for col in columns])

    def _map_to_dtos(self, entities):
        raise NotImplementedError


class HusSheetHandler(SheetHandler):

    def __init__(self, wb):
        super().__init__(wb, HusMapper(), HusSheetInfo())

    def _create_dto(self):
        return HusDto()

    def _map_to_dtos(self, entities):
        pass


class ForeldriSheetHandler(SheetHandler):

    def __init__(self, wb, husalisti):
        super().__init__(wb, ForeldriMapper(husalisti), ForeldriSheetInfo())

    def _create_dto(self):
        return ForeldriDto()

    def _map_to_dtos(self, entities):
        pass


class ThrifalistiSheetHandler(SheetHandler):
    def __init__(self, wb, husalisti):
        super().__init__(wb, ThrifalistiMapper(husalisti), ThrifalistiSheetInfo())
        self.__col_to_hus_map = self.init_col_to_hus_map()

    def init_col_to_hus_map(self):
        return {col.get_pos(): self.get_value(self._info.get_lykill_row(), col.get_pos()) for col in
                self._mapper.get_columns()}

    def _create_dto(self):
        return ThrifalistiDto()

    def _set_value(self, dto, col, val):
        if col.is_thrif():
            col.setter(dto, self.__col_to_hus_map[col.get_pos()], val)
        else:
            col.setter(dto, val)

    def write(self, entities):
        row_no = self._info.get_start_write_row_col()[0]
        for dto in self._map_to_dtos(entities):
            filtered_cols = list(filter(lambda c: filter_cols_before_start(c, self._info), self._mapper.get_columns()))
            for col in filtered_cols:
                self._sheet.cell(row_no, col.get_pos_num()).value = col.getter(dto, self.__col_to_hus_map[col.get_pos()])
            row_no += 1

    def _map_to_dtos(self, thrifalisti):
        dtos = [self._mapper.map_to_dto(thrifalisti.get_vikuthrifalisti(v.get_vika_nr()), self.__col_to_hus_map) for v in
                thrifalisti.get_vikuthrifalistar()]
        return dtos

    def reset(self):
        self._mapper.reset()
