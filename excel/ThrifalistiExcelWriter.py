class ThrifalistiVikaDto:
    def __init__(self, thrifalisti_i_viku, husalisti):
        husalisti_i_excel_rod = ["Rauða", "Ljósbláa", "Dökkbláa", "Græna", "Tóbíasar", "Skemman"]
        self.values = []
        for h in husalisti_i_excel_rod:
            self.values += [thrifalisti_i_viku[self.__get_key(h, husalisti)]]

    def __get_key(self, hus_nafn, husalisti):
        for h in husalisti:
            if h.get_nafn() == hus_nafn:
                return h


class ThrifalistiWriter:
    __START_ROW = 2
    __START_COL = 2

    def __init__(self, sheet):
        self.sheet = sheet
        self.row_no = self.__START_ROW

    def write_dto(self, dto):
        col = self.__START_COL

        if self.__is_haustfri():
            self.row_no += 1

        for v in dto.values:
            self.sheet.cell(self.row_no, col).value = v.get_nafn()
            col += 1

        self.row_no += 1

    def __is_haustfri(self):
        return "Haustfrí" in self.sheet.cell(self.row_no, 1).value
