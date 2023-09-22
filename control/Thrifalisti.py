from entity.VikuThrifalisti import VikuThrifalisti


class Thrifalisti:

    def __init__(self, vikuthrifalistar: [VikuThrifalisti]):
        vikuthrifalistar.sort(key=lambda v: v.get_vika_nr())
        self.__vikuthrifalistar: [VikuThrifalisti] = vikuthrifalistar

    def get_vikuthrifalistar(self):
        return self.__vikuthrifalistar

    def get_vikuthrifalisti(self, vika) -> VikuThrifalisti:
        return self.__vikuthrifalistar[vika]

    def is_full(self):
        return all([v.is_full() for v in self.__vikuthrifalistar])

