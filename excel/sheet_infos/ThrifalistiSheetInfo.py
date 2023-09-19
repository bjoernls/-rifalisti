from excel.dto.DtoFactory import ThrifalistiDtoFactory
from excel.sheet_infos.SheetInfo import SheetInfo


class ThrifalistiSheetInfo(SheetInfo):
    def get_sheet_name(self):
        return "Haust_2023"

    def get_workbook_name(self):
        return "Þrifalisti 2023.xlsx"

    def get_dto_factory(self, sheet):
        return ThrifalistiDtoFactory(sheet)

    def get_start_read_row_col(self):
        return [2, "A"]

    def get_start_write_row_col(self):
        return [2, "B"]
