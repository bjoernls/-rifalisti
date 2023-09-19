from entity.Foreldri import Foreldri
from entity.Hus import Hus
from entity.VikuThrifalisti import VikuThrifalisti
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

    def map_to_entity(self, hus_dto):
        return Hus(hus_dto.get_nafn(), exklusift=hus_dto.is_exclusive())


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
    __FRI = ["Haustfrí", "Jólafrí"]

    def __init__(self, husalisti):
        self.vika_nr = 0
        self.__husalisti = husalisti

    def map_to_dto(self, thrifalisti_fyrir_viku):
        dto = ThrifalistiDto()
        if thrifalisti_fyrir_viku.is_fri():
            return dto
        cols = dto.get_columns()
        for hus in self.__husalisti:
            col = next(filter(lambda c: hus.get_nafn() == c.get_id(), cols))
            col.setter(thrifalisti_fyrir_viku.get_foreldri_i_husi(hus).get_nafn())
        return dto

    def map_to_entity(self, dto):
        vika_texti = dto.get_vika_texti()
        vika = VikuThrifalisti(self.vika_nr, vika_texti,
                               self.__is_fri(vika_texti), self.__create_new_vikuthrifalisti(), self.__get_all_non_exclusive_hus())
        self.vika_nr += 1
        return vika

    def __get_all_non_exclusive_hus(self):
        return list(filter(lambda h: not h.is_exclusift(), self.__husalisti))

    def __is_fri(self, texti):
        return any(fri in texti for fri in self.__FRI)

    def __create_new_vikuthrifalisti(self):
        return {key: None for key in self.__husalisti}

    def reset(self):
        self.vika_nr = 0
