import openpyxl

from control.AlgorithmException import AlgorithmException
from control.Thrifalisti import Thrifalisti
from control.ThrifalistiAlgo import ThrifalistiAlgo
from excel.SheetHandler import HusSheetHandler, ThrifalistiSheetHandler, ForeldriSheetHandler, YfirlitSheetHandler, \
    StillingarSheetHandler


def compute(wb):
    i = 0

    stillingar = __get_stillingar(wb)
    # TODO listahandler
    husalisti = __get_husalisti(wb)
    foreldralisti = __get_foreldralisti(husalisti, wb)
    thrifalisti = __get_thrifalisti(foreldralisti, husalisti, wb)
    is_done = False

    while not is_done:
        i += 1

        try:
            ThrifalistiAlgo(foreldralisti, stillingar).compute(thrifalisti)
            is_done = True
        except AlgorithmException as e:
            print(e.get_message())
            foreldralisti, thrifalisti = __reset_listar(husalisti, wb)
            continue

        print(
            f"\nmin vikubil: {str(__calc_min_vikubil(foreldralisti))}, "
            f"max thrif count: {str(__calc_max_thrif_count(foreldralisti))}\n"
            f"{str(i)} runs"
        )

    write_to_excel_and_save(thrifalisti, foreldralisti, husalisti, wb)


def __reset_listar(husalisti, wb):
    foreldralisti = __get_foreldralisti(husalisti, wb)
    thrifalisti = __get_thrifalisti(foreldralisti, husalisti, wb)
    return foreldralisti, thrifalisti


def __get_thrifalisti(foreldralisti, husalisti, wb):
    return Thrifalisti(ThrifalistiSheetHandler(wb, husalisti, foreldralisti).read())


def __get_foreldralisti(husalisti, wb):
    return ForeldriSheetHandler(wb, husalisti).read()


def __get_stillingar(wb):
    return StillingarSheetHandler(wb).read()


def __get_husalisti(wb):
    return HusSheetHandler(wb).read()


def __calc_min_vikubil(foreldralisti):
    return min([f.get_vikubil() for f in list(filter(lambda f: f.get_vikubil() > 0, foreldralisti))])


def __calc_max_thrif_count(foreldralisti):
    return max([f.get_count() for f in foreldralisti])


def write_to_excel_and_save(thrifalisti, foreldralisti, husalisti, wb):
    YfirlitSheetHandler(wb).write(foreldralisti)
    ThrifalistiSheetHandler(wb, husalisti, foreldralisti).write(thrifalisti)
    wb.save("result.xlsx")


def calc_viku_fjoldi(vikuthrifalistar):
    return len(list(filter(lambda v: not v.is_fri(), vikuthrifalistar)))


if __name__ == '__main__':
    # compute(openpyxl.load_workbook("Testgögn.xlsx"))
    compute(openpyxl.load_workbook("Þrifalisti - Sniðmát.xlsx"))
