from excel.sheet_infos.SheetInfo import SheetInfo


class ForeldriSheetInfo(SheetInfo):
    def get_start_write_row_col(self):
        pass

    def get_sheet_name(self):
        return "Foreldralisti"

    def get_start_read_row_col(self):
        return [2, "B"]

    def get_name(self):
        pass

