class HusDto:

    def __init__(self):
        self.__nafn = None
        self.__is_exclusive = False

    def set_nafn(self, nafn):
        self.__nafn = nafn

    def get_nafn(self):
        return self.__nafn

    def is_exclusive(self):
        return self.__is_exclusive

    def set_exclusive(self, is_exclusive):
        if is_exclusive is None:
            return
        self.__is_exclusive = is_exclusive

    def __str__(self):
        return f'nafn: {self.__nafn}, exlusive: {self.__exclusive}'
