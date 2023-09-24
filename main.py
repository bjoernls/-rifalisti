import openpyxl

from control.Thrifalisti import Thrifalisti
from control.ThrifalistiAlgo import ThrifalistiAlgo
from excel.SheetHandler import HusSheetHandler, ThrifalistiSheetHandler, ForeldriSheetHandler


def print_sorted_foreldralisti(foreldralisti):
    foreldralisti.sort(key=lambda foreldri: foreldri.get_vikubil())
    for f in foreldralisti:
        print(f)


def compute(wb):
    i = 0

    husalisti = __get_husalisti(wb)
    foreldralisti = __get_foreldralisti(husalisti, wb)
    thrifalisti = __get_thrifalisti(foreldralisti, husalisti, wb)

    while True:
        i += 1

        ThrifalistiAlgo(foreldralisti).compute(thrifalisti)

        min_vikubil = __calc_min_vikubil(foreldralisti)
        print("min vikubil: " + str(min_vikubil))

        if min_vikubil >= 8:
            break
        else:
            foreldralisti, thrifalisti = __reset_listar(husalisti, wb)

    print(str(i) + " runs")

    write_to_excel_and_save(thrifalisti, ThrifalistiSheetHandler(wb, husalisti, foreldralisti), wb)


def __reset_listar(husalisti, wb):
    foreldralisti = __get_foreldralisti(husalisti, wb)
    thrifalisti = __get_thrifalisti(foreldralisti, husalisti, wb)
    return foreldralisti, thrifalisti


def __get_thrifalisti(foreldralisti, husalisti, wb):
    thrifalisti = Thrifalisti(ThrifalistiSheetHandler(wb, husalisti, foreldralisti).read())
    return thrifalisti


def __get_foreldralisti(husalisti, wb):
    foreldralisti = ForeldriSheetHandler(wb, husalisti).read()
    return foreldralisti


def __get_husalisti(wb):
    husalisti = HusSheetHandler(wb).read()
    return husalisti


def __calc_min_vikubil(foreldralisti):
    return min([f.get_vikubil() for f in list(filter(lambda f: f.get_vikubil() > 0, foreldralisti))])


def write_to_excel_and_save(thrifalisti, thrifalisti_sheet_handler, wb):
    thrifalisti_sheet_handler.write(thrifalisti)
    wb.save("result.xlsx")


def calc_viku_fjoldi(vikuthrifalistar):
    return len(list(filter(lambda v: not v.is_fri(), vikuthrifalistar)))


if __name__ == '__main__':
    compute(openpyxl.load_workbook("Testgögn.xlsx"))
