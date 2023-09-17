
class SheetInfo:
    def get_sheet_name(self):
        raise NotImplementedError()

    def get_workbook_name(self):
        raise NotImplementedError()

    def create_dto(self, sheet):
        raise NotImplementedError()

    def get_start_row_col(self):
        raise NotImplementedError()

    def get_name(self):
        raise NotImplementedError()
