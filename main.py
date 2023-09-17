import openpyxl

from control.ThrifalistiAlgo import ThrifalistiAlgo
from excel.SheetHandler import SheetHandler, ThrifalistiSheetHandler
from excel.ThrifalistiExcelWriter import ThrifalistiWriter, ThrifalistiVikaDto
from excel.sheet_infos.ForeldriSheetInfo import ForeldriSheetInfo
from excel.sheet_infos.HusSheetInfo import HusSheetInfo
from excel.sheet_infos.ThrifalistiSheetInfo import ThrifalistiSheetInfo
from mapper.Mapper import ForeldriMapper, ThrifalistiMapper
from mapper.Mapper import HusMapper


def print_sorted_foreldralisti(foreldralisti):
    foreldralisti.sort(key=lambda foreldri: foreldri.get_vikubil())
    for f in foreldralisti:
        print(f)


def compute(wb):
    min_vikubil = 0
    i = 0
    algo = None
    viku_fjoldi = 20
    hus_mapper = HusMapper(viku_fjoldi)

    while min_vikubil < 5:
        i += 1

        husalisti = SheetHandler(wb, HusSheetInfo()).read(hus_mapper)
        foreldralisti = SheetHandler(wb, ForeldriSheetInfo()).read(ForeldriMapper(husalisti))

        algo = ThrifalistiAlgo(husalisti, viku_fjoldi, foreldralisti)

        algo.compute()

        min_vikubil = min([f.get_vikubil() for f in list(filter(lambda f: f.get_vikubil() > 0, foreldralisti))])
        print("min vikubil: " + str(min_vikubil))

    print(str(i) + " runs")

    thrifalisti = algo.get_thrifalisti()

    t_mapper = ThrifalistiMapper()
    dtos = []

    for v in range(viku_fjoldi):
        dtos += [t_mapper.map_to_dto(thrifalisti.get_thrifalisti_i_viku(v))]

    ThrifalistiSheetHandler(wb, ThrifalistiSheetInfo()).write(dtos)

    print(thrifalisti)
    wb.save("result3.xlsx")


if __name__ == '__main__':
    compute(openpyxl.load_workbook("Þrifalisti 2023.xlsx"))
