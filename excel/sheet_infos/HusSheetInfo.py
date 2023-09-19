from excel.dto.DtoFactory import HusDtoFactory
from excel.dto.HusDto import HusDto
from excel.sheet_infos.SheetInfo import SheetInfo


class HusSheetInfo(SheetInfo):
    def get_sheet_name(self):
        return "Húsalisti"

    def get_workbook_name(self):
        return "Þrifalisti 2023.xlsx"

    def get_dto_factory(self, sheet):
        return HusDtoFactory(sheet)

    def get_start_read_row_col(self):
        return [2, "A"]

    def get_start_write_row_col(self):
        raise NotImplementedError
