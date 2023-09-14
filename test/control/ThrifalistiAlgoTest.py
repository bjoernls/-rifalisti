import unittest

from entity.Foreldri import Foreldri
from entity.Hus import Hus
from control.ThrifalistiAlgo import ThrifalistiAlgo


class MyTestCase(unittest.TestCase):

    def test_algo_compute(self):
        viku_fjoldi = 20
        husalisti = [Hus("a", viku_fjoldi), Hus("b", viku_fjoldi), Hus("c", viku_fjoldi), Hus("d", viku_fjoldi),
                     Hus("e", viku_fjoldi), Hus("f", viku_fjoldi)]
        foreldralisti = []
        for i in range(60):
            foreldralisti += [Foreldri("f" + str(i), husalisti)]

        algo = ThrifalistiAlgo(husalisti, viku_fjoldi, foreldralisti)

        algo.compute()

        thrifalisti = algo.get_thrifalisti()

        self.assertIsNotNone(thrifalisti)
        print(thrifalisti)

        self.print_sorted_foreldralisti(foreldralisti)

        # feilar oftast:
        # self.assertLessEqual(self.calculate_count_diff(foreldralisti), 1)

        self.assert_one_slot_per_week(husalisti, thrifalisti, viku_fjoldi)

    def print_sorted_foreldralisti(self, foreldralisti):
        foreldralisti.sort(key=lambda foreldri: foreldri.get_vikubil())
        for f in foreldralisti:
            print(f)

    def test_run_until_min_vikubil(self):
        min_vikubil = 0
        i = 0
        algo = None
        foreldralisti = None
        while min_vikubil < 10:
            i += 1
            viku_fjoldi = 20
            husalisti = [Hus("a", viku_fjoldi, exklusift=True), Hus("b", viku_fjoldi, exklusift=True),
                         Hus("c", viku_fjoldi), Hus("d", viku_fjoldi), Hus("e", viku_fjoldi), Hus("f", viku_fjoldi)]
            foreldralisti = self.init_foreldralisti(husalisti)

            algo = ThrifalistiAlgo(husalisti, viku_fjoldi, foreldralisti)

            algo.compute()

            min_vikubil = min([f.get_vikubil() for f in list(filter(lambda f: f.get_vikubil() > 0, foreldralisti))])
            print("min vikubil: " + str(min_vikubil))

        print(str(i) + " runs")

        thrifalisti = algo.get_thrifalisti()

        print(thrifalisti)
        self.print_sorted_foreldralisti(foreldralisti)

    def test_algo_compute_with_exclusive_hus(self):
        viku_fjoldi = 20
        husalisti = [Hus("a", viku_fjoldi, exklusift=True), Hus("b", viku_fjoldi, exklusift=True),
                     Hus("c", viku_fjoldi), Hus("d", viku_fjoldi), Hus("e", viku_fjoldi), Hus("f", viku_fjoldi)]
        foreldralisti = self.init_foreldralisti(husalisti)

        algo = ThrifalistiAlgo(husalisti, viku_fjoldi, foreldralisti)

        algo.compute()

        thrifalisti = algo.get_thrifalisti()

        print(thrifalisti)
        self.print_sorted_foreldralisti(foreldralisti)

        self.test_exclusivity(husalisti, thrifalisti, viku_fjoldi)

    def init_foreldralisti(self, husalisti):
        foreldralisti = []
        for i in range(10):
            foreldralisti += [Foreldri("a" + str(i), [husalisti[0]])]

        for i in range(15):
            foreldralisti += [Foreldri("b" + str(i), [husalisti[1]])]

        for i in range(40):
            foreldralisti += [Foreldri("c" + str(i), husalisti[2:])]
        return foreldralisti

    def calculate_count_diff(self, foreldralisti):
        return max([f.get_count() for f in foreldralisti]) - min([f.get_count() for f in foreldralisti])

    def test_exclusivity(self, husalisti, thrifalisti, viku_fjoldi):
        for vika in range(viku_fjoldi):
            self.assertTrue("a" in thrifalisti.get_foreldri(vika, husalisti[0]).get_nafn())
            self.assertTrue("b" in thrifalisti.get_foreldri(vika, husalisti[1]).get_nafn())

    def assert_one_slot_per_week(self, husalisti, thrifalisti, viku_fjoldi):
        for vika in range(viku_fjoldi):
            foreldri_i_viku = []
            for hus in husalisti:
                foreldri_i_viku += [thrifalisti.get_foreldri(vika, hus)]
            self.assertEqual(len(set(foreldri_i_viku)), len(husalisti))


if __name__ == '__main__':
    unittest.main()
