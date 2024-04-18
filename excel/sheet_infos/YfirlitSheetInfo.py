from excel.sheet_infos.SheetInfo import SheetInfo


class YfirlitSheetInfo(SheetInfo):
    def get_sheet_name(self):
        return "Yfirlit"

    def get_start_read_row_col(self):
        return [3, "A"]

    def get_start_write_row_col(self):
        return [3, "A"]

    def get_lykill_row(self):
        return 2
