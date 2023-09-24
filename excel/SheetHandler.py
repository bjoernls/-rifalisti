from excel.Column import Column
from excel.SheetReader import SheetReader, ThrifalistiSheetReader, get_sheet_value
from excel.SheetWriter import ThrifalistiSheetWriter
from excel.dto.ForeldriDto import ForeldriDto
from excel.dto.HusDto import HusDto
from excel.dto.ThrifalistiDto import ThrifalistiDto, ThrifalistiColumn
from excel.sheet_infos.ForeldriSheetInfo import ForeldriSheetInfo
from excel.sheet_infos.HusSheetInfo import HusSheetInfo
from excel.sheet_infos.ThrifalistiSheetInfo import ThrifalistiSheetInfo
from mapper.Mapper import HusMapper, ForeldriMapper, ThrifalistiMapper


class SheetHandler:

    def __init__(self, wb, info):
        self._sheet = wb[info.get_sheet_name()]
        self._info = info
        self._mapper = self._get_mapper()
        self._reader = self._init_reader()
        self._writer = self._init_writer()

    def read(self):
        return self._reader.read()

    def write(self, entities):
        if not self._writer:
            raise NotImplementedError
        return self._writer.write(entities)

    def _get_columns(self):
        raise NotImplementedError

    def _init_reader(self):
        return SheetReader(self._sheet, self._mapper, self._info, self._get_columns(), self._get_dto_factory())

    def _get_dto_factory(self):
        raise NotImplementedError

    def _get_mapper(self):
        raise NotImplementedError

    def _init_writer(self):
        return None


class HusSheetHandler(SheetHandler):

    def __init__(self, wb):
        super().__init__(wb, HusSheetInfo())

    def _get_columns(self):
        columns = [Column("A", lambda args: args[0].set_nafn(args[1]), lambda args: args[0].get_nafn())]
        columns += \
            [Column("B", lambda args: args[0].set_exclusive(args[1]), lambda args: args[0].is_exclusive())]
        return columns

    def _get_dto_factory(self):
        return lambda: HusDto()

    def _get_mapper(self):
        return HusMapper()


class ForeldriSheetHandler(SheetHandler):

    def __init__(self, wb, husalisti):
        self.__husalisti = husalisti
        super().__init__(wb, ForeldriSheetInfo())

    def _get_mapper(self):
        return ForeldriMapper(self.__husalisti)

    def _get_columns(self):
        columns = [Column("B", lambda args: args[0].set_nafn(args[1]), lambda args: args[0].get_nafn())]
        columns += \
            [Column("C", lambda args: args[0].set_thrifastada(args[1]), lambda args: args[0].get_thrifastada())]
        columns += [Column("D", lambda args: args[0].add_hus(args[1]), lambda args: args[0].get_husalisti())]
        columns += [Column("E", lambda args: args[0].add_hus(args[1]), lambda args: args[0].get_husalisti())]
        columns += [Column("F", lambda args: args[0].add_hus(args[1]), lambda args: args[0].get_husalisti())]
        return columns

    def _get_dto_factory(self):
        return lambda: ForeldriDto()


class ThrifalistiSheetHandler(SheetHandler):
    def __init__(self, wb, husalisti, foreldralisti):
        self.__foreldralisti = foreldralisti
        self.__husalisti = husalisti
        self.__col_to_hus_map = {}
        super().__init__(wb, ThrifalistiSheetInfo())

    def _get_dto_factory(self):
        return lambda: ThrifalistiDto()

    def _get_mapper(self):
        return ThrifalistiMapper(self.__husalisti, self.__foreldralisti, self._get_columns(),
                                 self.__get_col_to_hus_map(self._info))

    def _init_reader(self):
        return ThrifalistiSheetReader(self._sheet, self._mapper, self._info,
                                      self._get_columns(), self._get_dto_factory(),
                                      self.__get_col_to_hus_map(self._info))

    def _init_writer(self):
        return ThrifalistiSheetWriter(self._sheet, self._mapper, self._info, self._get_columns(),
                                      self.__get_col_to_hus_map(self._info))

    def __get_col_to_hus_map(self, info):
        if not self.__col_to_hus_map:
            self.__col_to_hus_map = {
                col.get_pos(): get_sheet_value(self._sheet, col.get_pos(), info.get_lykill_row())
                for col in self._get_columns()}
        return self.__col_to_hus_map

    def _get_columns(self):
        columns = [
            ThrifalistiColumn("A", lambda args: args[0].set_vika_texti(args[1]), lambda dto: dto.get_vika_texti())]

        for s in range(ord("B"), ord("G") + 1):
            col_stafur = chr(s)
            columns += [
                ThrifalistiColumn(col_stafur, lambda args: args[0].add_to_thrifalisti(args[1], args[2]),
                                  lambda args: args[0].get_thrif(args[1]), is_thrif=True)]
        return columns
