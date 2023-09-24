def convert_to_num(col):
    return ord(col.lower()) - 96


class Column:
    def __init__(self, pos, setter, getter):
        self.__pos = pos
        self.__setter = setter
        self.__getter = getter

    def getter(self, *args):
        return self.__getter(args)

    def setter(self, *val):
        self.__setter(val)

    def get_pos(self):
        return self.__pos

    def get_pos_num(self):
        return convert_to_num(self.get_pos())
