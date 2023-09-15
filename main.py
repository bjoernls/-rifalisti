from control.ThrifalistiAlgo import ThrifalistiAlgo
from entity.Foreldri import Foreldri
from entity.Hus import Hus


def init_foreldralisti(husalisti):
    foreldralisti = []
    for i in range(10):
        foreldralisti += [Foreldri("a" + str(i), [husalisti[0]])]

    for i in range(15):
        foreldralisti += [Foreldri("b" + str(i), [husalisti[1]])]

    for i in range(40):
        foreldralisti += [Foreldri("c" + str(i), husalisti[2:])]
    return foreldralisti


def print_sorted_foreldralisti(foreldralisti):
    foreldralisti.sort(key=lambda foreldri: foreldri.get_vikubil())
    for f in foreldralisti:
        print(f)


def run_until_min_vikubil_reached():
    min_vikubil = 0
    i = 0
    algo = None
    foreldralisti = None
    while min_vikubil < 10:
        i += 1
        viku_fjoldi = 20
        husalisti = [Hus("a", viku_fjoldi, exklusift=True), Hus("b", viku_fjoldi, exklusift=True),
                     Hus("c", viku_fjoldi), Hus("d", viku_fjoldi), Hus("e", viku_fjoldi), Hus("f", viku_fjoldi)]
        foreldralisti = init_foreldralisti(husalisti)

        algo = ThrifalistiAlgo(husalisti, viku_fjoldi, foreldralisti)

        algo.compute()

        min_vikubil = min([f.get_vikubil() for f in list(filter(lambda f: f.get_vikubil() > 0, foreldralisti))])
        print("min vikubil: " + str(min_vikubil))

    thrifalisti = algo.get_thrifalisti()

    print(thrifalisti)
    print_sorted_foreldralisti(foreldralisti)

    print(str(i) + " runs")


if __name__ == '__main__':
    run_until_min_vikubil_reached()
