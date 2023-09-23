from excel.dto.Column import convert_to_num, Column
from excel.dto.ForeldriDto import ForeldriDto
from excel.dto.HusDto import HusDto
from excel.dto.ThrifalistiDto import ThrifalistiDto, ThrifalistiColumn
from excel.sheet_infos.ForeldriSheetInfo import ForeldriSheetInfo
from excel.sheet_infos.HusSheetInfo import HusSheetInfo
from excel.sheet_infos.ThrifalistiSheetInfo import ThrifalistiSheetInfo
from mapper.Mapper import HusMapper, ForeldriMapper, ThrifalistiMapper


class SheetHandler:

    @staticmethod
    def __convert_to_num(col):
        return ord(col.lower()) - 96

    @staticmethod
    def filter_cols_before_start(column, info):
        return ord(column.get_pos()) >= ord(info.get_start_write_row_col()[1])

    def __init__(self, wb, mapper, info):
        self._sheet = wb[info.get_sheet_name()]
        self._mapper = mapper
        self._info = info

    def read(self):
        self._mapper.reset()
        return [self._mapper.map_to_entity(dto) for dto in self._create_dtos()]

    def write(self, entities):
        row_no = self._info.get_start_write_row_col()[0]
        for dto in self._map_to_dtos(entities):
            filtered_cols = list(filter(lambda c: self.filter_cols_before_start(c, self._info), self._get_columns()))
            for col in filtered_cols:
                self._set_sheet_value(row_no, col.get_pos(), self._get_write_value(dto, col))
            row_no += 1

    def _get_write_value(self, dto, col: Column):
        pass

    def _get_sheet_value(self, row, col):
        return self._sheet.cell(row, convert_to_num(col)).value

    def _set_sheet_value(self, row, col, value):
        self._sheet.cell(row, convert_to_num(col)).value = value

    def _create_dtos(self):
        dtos = []

        columns = self._get_columns()
        row = self._info.get_start_read_row_col()[0]

        while not self.__is_row_empty(row, columns):
            dto = self._create_dto()
            for col in columns:
                val = self._get_sheet_value(row, col.get_pos())
                self._set_value(dto, col, val)
            row += 1
            dtos += [dto]

        return dtos

    def _set_value(self, dto, col, val):
        col.setter(dto, val)

    def _create_dto(self):
        raise NotImplementedError

    def __is_row_empty(self, row, columns):
        return all([self._get_sheet_value(row, col.get_pos()) is None for col in columns])

    def _map_to_dtos(self, entities):
        raise NotImplementedError

    def _get_columns(self):
        raise NotImplementedError


class HusSheetHandler(SheetHandler):

    def __init__(self, wb):
        super().__init__(wb, HusMapper(), HusSheetInfo())
        self.__columns = []

    def _create_dto(self):
        return HusDto()

    def _map_to_dtos(self, entities):
        pass

    def _get_columns(self):
        if not self.__columns:
            self.__columns = [Column("A", lambda args: args[0].set_nafn(args[1]), lambda args: args[0].get_nafn())]
            self.__columns += \
                [Column("B", lambda args: args[0].set_exclusive(args[1]), lambda args: args[0].is_exclusive())]
        return self.__columns


class ForeldriSheetHandler(SheetHandler):

    def __init__(self, wb, husalisti):
        super().__init__(wb, ForeldriMapper(husalisti), ForeldriSheetInfo())
        self.columns = []

    def _get_columns(self):
        if not self.columns:
            self.columns = [Column("B", lambda args: args[0].set_nafn(args[1]), lambda args: args[0].get_nafn())]
            self.columns += \
                [Column("C", lambda args: args[0].set_thrifastada(args[1]), lambda args: args[0].get_thrifastada())]
            self.columns += [Column("D", lambda args: args[0].add_hus(args[1]), lambda args: args[0].get_husalisti())]
            self.columns += [Column("E", lambda args: args[0].add_hus(args[1]), lambda args: args[0].get_husalisti())]
            self.columns += [Column("F", lambda args: args[0].add_hus(args[1]), lambda args: args[0].get_husalisti())]
        return self.columns

    def _create_dto(self):
        return ForeldriDto()

    def _map_to_dtos(self, entities):
        pass


class ThrifalistiSheetHandler(SheetHandler):
    def __init__(self, wb, husalisti, foreldralisti):
        super().__init__(wb, None, ThrifalistiSheetInfo())
        self.__columns = []
        self.__col_to_hus_map = {}
        self._mapper = self.__get_mapper(husalisti, foreldralisti)

    def __get_mapper(self, husalisti, foreldralisti):
        return ThrifalistiMapper(husalisti, foreldralisti, self._get_columns(), self.__get_col_to_hus_map())

    def __get_col_to_hus_map(self):
        if not self.__col_to_hus_map:
            self.__col_to_hus_map = {
                col.get_pos(): self._get_sheet_value(ThrifalistiSheetInfo().get_lykill_row(), col.get_pos())
                for col in self._get_columns()}
        return self.__col_to_hus_map

    def _get_columns(self):
        if not self.__columns:
            self.__columns = [
                ThrifalistiColumn("A", lambda args: args[0].set_vika_texti(args[1]), lambda dto: dto.get_vika_texti())]

            for s in range(ord("B"), ord("G") + 1):
                col_stafur = chr(s)
                self.__columns += [ThrifalistiColumn(col_stafur, lambda args: args[0].add_to_thrifalisti(args[1], args[2]),
                                      lambda args: args[0].get_thrif(args[1]), is_thrif=True)]
        return self.__columns

    def _create_dto(self):
        return ThrifalistiDto()

    def _set_value(self, dto, col, val):
        if col.is_thrif():
            col.setter(dto, self.__col_to_hus_map[col.get_pos()], val)
        else:
            col.setter(dto, val)

    def _get_write_value(self, dto, col: Column):
        return col.getter(dto, self.__get_col_to_hus_map()[col.get_pos()])

    def _map_to_dtos(self, thrifalisti):
        dtos = [self._mapper.map_to_dto(thrifalisti.get_vikuthrifalisti(v.get_vika_nr()))
                for v in thrifalisti.get_vikuthrifalistar()]
        return dtos

    def reset(self):
        self._mapper.reset()
