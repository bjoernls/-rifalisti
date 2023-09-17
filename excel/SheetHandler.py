from excel.dto.DtoIterator import DtoIterator
from mapper.Mapper import Mapper


class SheetHandler:

    def __get_sheet(self, wb, info):
        return wb[info.get_sheet_name()]

    def read(self, wb, info, mapper: Mapper):
        return [mapper.map_to_entity(dto) for dto in DtoIterator(self.__get_sheet(wb, info), info)]

    def write(self, dtos):
        pass