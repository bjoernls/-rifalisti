from random import randint


class Strategy:
    def compute(self, size):
        raise NotImplementedError()


class RandomStrategy(Strategy):
    def compute(self, size):
        return randint(0, size - 1)


class RoundRobinStrategy(Strategy):
    def compute(self, _):
        return 0
