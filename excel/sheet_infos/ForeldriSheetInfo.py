from excel.dto.DtoFactory import ForeldriDtoFactory
from excel.sheet_infos.SheetInfo import SheetInfo
from excel.dto.ForeldriDto import ForeldriDto


class ForeldriSheetInfo(SheetInfo):
    def get_sheet_name(self):
        return "Foreldralisti"

    def get_workbook_name(self):
        return "Þrifalisti 2023.xlsx"

    def create_dto(self, sheet):
        factory = ForeldriDtoFactory(sheet)
        return lambda row: factory.create_dto(row)

    def get_start_read_row_col(self):
        return [2, "B"]

    def get_name(self):
        pass

