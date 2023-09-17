import openpyxl


class WbManager:

    def __init__(self):
        self.workbooks = {}

    def open_wb(self, wb_name):
        if wb_name not in self.workbooks:
            wb = openpyxl.load_workbook(wb_name)
            self.workbooks[wb_name] = wb
        else:
            wb = self.workbooks[wb_name]
        return wb
