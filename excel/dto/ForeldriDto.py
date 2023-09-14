from entity.Foreldri import Foreldri


class ForeldriDto:
    def __init__(self):
        self.nafn = ""
        self.level = 0
        self.pref_hus = [] # hús sem foreldri vill, tómt ef alveg sama


# mappar Dto yfir í Foreldri-object
class ForeldriDtoMapper:
    def __init__(self, huslisti):
        self.huslisti = huslisti

    def map(self, dto: ForeldriDto):
        if dto.pref_hus is None or len(dto.pref_hus) == 0:
            pref_huslisti = self.huslisti
        else:
            pref_huslisti = dto.pref_hus
        return Foreldri(dto.nafn, pref_huslisti)


