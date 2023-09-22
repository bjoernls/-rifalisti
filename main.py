import openpyxl

from control.Thrifalisti import Thrifalisti
from control.ThrifalistiAlgo import ThrifalistiAlgo
from excel.SheetHandler import HusSheetHandler, ThrifalistiSheetHandler, ForeldriSheetHandler


def print_sorted_foreldralisti(foreldralisti):
    foreldralisti.sort(key=lambda foreldri: foreldri.get_vikubil())
    for f in foreldralisti:
        print(f)


def compute(wb):
    min_vikubil = 0
    i = 0

    husalisti = HusSheetHandler(wb).read()
    thrifalisti_sheet_handler = ThrifalistiSheetHandler(wb, husalisti)
    thrifalisti = None

    while min_vikubil < 8:
        i += 1
        thrifalisti = Thrifalisti(thrifalisti_sheet_handler.read())

        foreldralisti = ForeldriSheetHandler(wb, husalisti).read()

        ThrifalistiAlgo(foreldralisti).compute(thrifalisti)

        min_vikubil = __calc_min_vikubil(foreldralisti)
        print("min vikubil: " + str(min_vikubil))

    print(str(i) + " runs")

    write_to_excel_and_save(thrifalisti, thrifalisti_sheet_handler, wb)


def __calc_min_vikubil(foreldralisti):
    return min([f.get_vikubil() for f in list(filter(lambda f: f.get_vikubil() > 0, foreldralisti))])


def write_to_excel_and_save(thrifalisti, thrifalisti_sheet_handler, wb):
    thrifalisti_sheet_handler.write(thrifalisti)
    wb.save("result.xlsx")


def calc_viku_fjoldi(vikuthrifalistar):
    return len(list(filter(lambda v: not v.is_fri(), vikuthrifalistar)))


if __name__ == '__main__':
    compute(openpyxl.load_workbook("Testgögn.xlsx"))
