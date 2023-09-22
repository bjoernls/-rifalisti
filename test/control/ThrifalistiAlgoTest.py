import unittest

from control.ThrifalistiAlgo import ThrifalistiAlgo
from entity.Foreldri import Foreldri
from entity.Hus import Hus


class MyTestCase(unittest.TestCase):

    def test_algo_compute(self):
        viku_fjoldi = 20
        husalisti = [Hus("a", viku_fjoldi), Hus("b", viku_fjoldi), Hus("c", viku_fjoldi), Hus("d", viku_fjoldi),
                     Hus("e", viku_fjoldi), Hus("f", viku_fjoldi)]
        foreldralisti = []
        for i in range(60):
            foreldralisti += [Foreldri("f" + str(i), husalisti)]

        algo = ThrifalistiAlgo(viku_fjoldi)

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

    def test_algo_compute_with_exclusive_hus(self):
        viku_fjoldi = 20
        husalisti = [Hus("a", viku_fjoldi, exklusift=True), Hus("b", viku_fjoldi, exklusift=True),
                     Hus("c", viku_fjoldi), Hus("d", viku_fjoldi), Hus("e", viku_fjoldi), Hus("f", viku_fjoldi)]
        foreldrar_med_auka_thrif = ["c2", "c8", "a1"]
        foreldralisti = self.init_foreldralisti(husalisti, foreldrar_med_auka_thrif)

        algo = ThrifalistiAlgo(viku_fjoldi)

        algo.compute()

        thrifalisti = algo.get_thrifalisti()

        print(thrifalisti)
        self.print_sorted_foreldralisti(foreldralisti)

        for f in list(filter(lambda f2: f2.get_nafn() in foreldrar_med_auka_thrif, foreldralisti)):
            self.assertTrue(f.get_count(), 3)

        self.test_exclusivity(husalisti, thrifalisti, viku_fjoldi)

    def init_foreldralisti(self, husalisti, foreldrar_med_auka_thrif=[]):
        foreldralisti = []
        for i in range(9):
            nafn = "a" + str(i)
            foreldralisti += [Foreldri(nafn, [husalisti[0]], has_auka_thrif=nafn in foreldrar_med_auka_thrif)]

        for i in range(15):
            nafn = "b" + str(i)
            foreldralisti += [Foreldri(nafn, [husalisti[1]], has_auka_thrif=nafn in foreldrar_med_auka_thrif)]

        for i in range(30):
            nafn = "c" + str(i)
            foreldralisti += [Foreldri(nafn, husalisti[2:], has_auka_thrif=nafn in foreldrar_med_auka_thrif)]

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
