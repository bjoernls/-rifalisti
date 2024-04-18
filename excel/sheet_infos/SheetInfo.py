
class SheetInfo:
    def get_sheet_name(self):
        raise NotImplementedError()

    def get_start_read_row_col(self):
        raise NotImplementedError()

    def get_start_write_row_col(self):
        raise NotImplementedError()

