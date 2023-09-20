import openpyxl

from control.Thrifalisti import Thrifalisti
from control.ThrifalistiAlgo import ThrifalistiAlgo
from excel.SheetHandler import SheetHandler
from excel.sheet_infos.ForeldriSheetInfo import ForeldriSheetInfo
from excel.sheet_infos.HusSheetInfo import HusSheetInfo
from excel.sheet_infos.ThrifalistiSheetInfo import ThrifalistiSheetInfo
from mapper.Mapper import ThrifalistiMapper, ForeldriMapper
from mapper.Mapper import HusMapper


def print_sorted_foreldralisti(foreldralisti):
    foreldralisti.sort(key=lambda foreldri: foreldri.get_vikubil())
    for f in foreldralisti:
        print(f)


def compute(wb):
    min_vikubil = 0
    i = 0

    husalisti = SheetHandler(wb, HusSheetInfo()).read(HusMapper())
    tl_mapper = ThrifalistiMapper(husalisti)
    thrifalisti = None
    tl_sheet_handler = SheetHandler(wb, ThrifalistiSheetInfo())

    while min_vikubil < 8:
        i += 1
        foreldralisti = SheetHandler(wb, ForeldriSheetInfo()).read(ForeldriMapper(husalisti))

        vikuthrifalistar = tl_sheet_handler.read(tl_mapper)
        thrifalisti = Thrifalisti(vikuthrifalistar)

        ThrifalistiAlgo(foreldralisti).compute(thrifalisti)

        min_vikubil = min([f.get_vikubil() for f in list(filter(lambda f: f.get_vikubil() > 0, foreldralisti))])
        print("min vikubil: " + str(min_vikubil))

        tl_mapper.reset()

    print(str(i) + " runs")

    write_to_excel_and_save(thrifalisti, tl_mapper, tl_sheet_handler, wb)


def write_to_excel_and_save(thrifalisti, tl_mapper, tl_sheet_handler, wb):
    tl_sheet_handler.write(__create_thrifalisti_dtos(thrifalisti, tl_mapper))
    wb.save("result2.xlsx")


def calc_viku_fjoldi(vikuthrifalistar):
    return len(list(filter(lambda v: not v.is_fri(), vikuthrifalistar)))


def __create_thrifalisti_dtos(thrifalisti, tl_mapper):
    dtos = [tl_mapper.map_to_dto(thrifalisti.get_vikuthrifalisti(v.get_vika_nr())) for v in thrifalisti.get_vikuthrifalistar()]
    return dtos


if __name__ == '__main__':
    compute(openpyxl.load_workbook("Þrifalisti 2023.xlsx"))
