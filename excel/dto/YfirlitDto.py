from entity.Allocation import Allocation


class YfirlitDto:
    def __init__(self, nafn, count, allocs):
        self.nafn = nafn
        self.count = count
        self.allocs: [Allocation] = allocs
        allocs.sort(key=lambda a: a.get_vika())

    def get_nafn(self):
        return self.nafn

    def get_count(self):
        return self.count

    def get_alloc_vika(self, i):
        if i >= len(self.allocs):
            return ""
        return self.allocs[i].get_vika_texti()

    def get_alloc_hus(self, i):
        if i >= len(self.allocs):
            return ""
        return self.allocs[i].get_hus().get_nafn()
