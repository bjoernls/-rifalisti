from entity.Foreldri import Foreldri
from entity.Hus import Hus
from entity.Vika import Vika
from excel.dto.ForeldriDto import ForeldriDto
from excel.dto.ThrifalistiDto import ThrifalistiDto


class Mapper:

    def map_to_entity(self, dto):
        raise NotImplementedError

    def map_to_dto(self, entity):
        raise NotImplementedError


class HusMapper(Mapper):

    def map_to_dto(self, entity):
        pass

    def __init__(self, vikufjoldi):
        self.vikufjoldi = vikufjoldi

    def map_to_entity(self, hus_dto):
        return Hus(hus_dto.get_nafn(), self.vikufjoldi, exklusift=hus_dto.is_exclusive())


class ForeldriMapper(Mapper):

    def map_to_dto(self, entity):
        pass

    def __init__(self, husalisti):
        self.husalisti = husalisti

    def __map_hus(self, hus_nafn, husalisti):
        for h in husalisti:
            if h.get_nafn() == hus_nafn:
                return h
        raise ValueError

    def map_to_entity(self, foreldri_dto: ForeldriDto) -> Foreldri:
        husalisti_mapped = list(map(lambda h: self.__map_hus(h, self.husalisti), foreldri_dto.get_husalisti()))
        if len(husalisti_mapped) == 0:
            husalisti_mapped = list(filter(lambda h: not h.is_exclusift(), self.husalisti))
        return Foreldri(foreldri_dto.get_nafn(), husalisti_mapped, foreldri_dto.has_less_thrif(),
                        foreldri_dto.has_auka_thrif())


class ThrifalistiMapper(Mapper):

    def __init__(self):
        self.vika_nr = 0

    def map_to_dto(self, thrifalisti_fyrir_viku):
        dto = ThrifalistiDto()
        cols = dto.get_columns()
        for hus in thrifalisti_fyrir_viku:
            col = next(filter(lambda c: hus.get_nafn() == c.get_id(), cols))
            col.setter(thrifalisti_fyrir_viku[hus].get_nafn())
        return dto

    def map_to_entity(self, dto):
        vika = Vika(self.vika_nr, dto.get_vika_texti(), {key: [] for key in self.husalisti_i_excel_rod})
        self.vika_nr += 1
        return vika
