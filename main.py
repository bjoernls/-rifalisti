import openpyxl

from control.Thrifalisti import Thrifalisti
from control.ThrifalistiAlgo import ThrifalistiAlgo
from excel.SheetHandler import SheetHandler, ThrifalistiSheetHandler
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
    vikulisti = []
    thrifalisti = None

    while min_vikubil < 8:
        i += 1
        vikulisti = SheetHandler(wb, ThrifalistiSheetInfo()).read(tl_mapper)
        viku_fjoldi = len(list(filter(lambda v: not v.is_fri(), vikulisti)))

        thrifalisti = Thrifalisti(vikulisti, husalisti)

        foreldralisti = SheetHandler(wb, ForeldriSheetInfo()).read(ForeldriMapper(husalisti))

        algo = ThrifalistiAlgo(husalisti, viku_fjoldi, foreldralisti)

        algo.compute(thrifalisti)

        min_vikubil = min([f.get_vikubil() for f in list(filter(lambda f: f.get_vikubil() > 0, foreldralisti))])
        print("min vikubil: " + str(min_vikubil))

        tl_mapper.reset()

    print(str(i) + " runs")

    dtos = []

    for v in vikulisti:
        dtos += [tl_mapper.map_to_dto(thrifalisti.get_thrifalisti_i_viku(v.get_vika_nr()))]

    ThrifalistiSheetHandler(wb, ThrifalistiSheetInfo()).write(dtos)

    wb.save("result.xlsx")


if __name__ == '__main__':
    compute(openpyxl.load_workbook("Þrifalisti 2023.xlsx"))
