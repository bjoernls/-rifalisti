from excel.dto.DtoFactory import HusDtoFactory
from excel.dto.HusDto import HusDto
from excel.sheet_infos.SheetInfo import SheetInfo


class HusSheetInfo(SheetInfo):
    def get_sheet_name(self):
        return "Húsalisti"

    def get_workbook_name(self):
        return "Þrifalisti 2023.xlsx"

    def create_dto(self, sheet):
        factory = HusDtoFactory(sheet)
        return lambda row: factory.create_dto(row)

    def get_start_row_col(self):
        return [2, "A"]

    def get_name(self):
        pass
