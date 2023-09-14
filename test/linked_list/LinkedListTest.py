import unittest

from entity.Foreldri import Foreldri
from linked_list.LinkedList import LinkedList


def create_test_data():
    result = LinkedList([])
    result.push(Foreldri("A", []))
    result.push(Foreldri("B", []))
    result.push(Foreldri("C", []))
    result.push(Foreldri("D", []))
    return result


class MyTestCase(unittest.TestCase):

    def test_LinkedList_push(self):
        linked_list = create_test_data()
        self.assertEqual(linked_list.head.data.get_nafn(), "A")
        self.assertEqual(linked_list.head.next.data.get_nafn(), "B")
        self.assertEqual(linked_list.head.next.next.data.get_nafn(), "C")
        self.assertEqual(linked_list.head.next.next.next.data.get_nafn(), "D")
        self.assertEqual(linked_list.head.next.next.next.next, None)

    def test_LinkedList_pop_first(self):
        linked_list = create_test_data()

        self.assertEqual(linked_list.pop(0).get_nafn(), "A")
        self.assertEqual(linked_list.head.data.get_nafn(), "B")

    def assert_linked_list_order(self, linked_list, nodes):
        i = 0
        node = linked_list.head
        while node is not None:
            self.assertEqual(node.data.get_nafn(), nodes[i])
            i += 1
            node = node.next

    def test_push_none(self):
        with self.assertRaises(ValueError):
            LinkedList([]).push(None)

    def test_LinkedList_pop_oob(self):
        linked_list = create_test_data()

        self.assertEqual(linked_list.get_size(), 4)
        self.assert_linked_list_order(linked_list, ["A", "B", "C", "D"])

        with self.assertRaises(ValueError):
            linked_list.pop(4)

    def test_LinkedList_pop_last(self):
        linked_list = create_test_data()

        self.assertEqual(linked_list.get_size(), 4)
        self.assert_linked_list_order(linked_list, ["A", "B", "C", "D"])

        self.assertEqual(linked_list.pop(3).get_nafn(), "D")

        self.assert_linked_list_order(linked_list, ["A", "B", "C"])
        self.assertEqual(linked_list.head.data.get_nafn(), "A")
        self.assertEqual(linked_list.head.next.data.get_nafn(), "B")
        self.assertEqual(linked_list.get_size(), 3)

    def test_LinkedList_pop_any(self):
        linked_list = create_test_data()

        self.assertEqual(linked_list.get_size(), 4)

        self.assertEqual(linked_list.pop(1).get_nafn(), "B")

        self.assert_linked_list_order(linked_list, ["A", "C", "D"])
        self.assertEqual(linked_list.head.data.get_nafn(), "A")
        self.assertEqual(linked_list.head.next.data.get_nafn(), "C")
        self.assertEqual(linked_list.get_size(), 3)

        self.assertEqual(linked_list.pop(1).get_nafn(), "C")

        self.assert_linked_list_order(linked_list, ["A", "D"])
        self.assertEqual(linked_list.head.data.get_nafn(), "A")
        self.assertEqual(linked_list.head.next.data.get_nafn(), "D")
        self.assertEqual(linked_list.get_size(), 2)

        self.assertEqual(linked_list.pop(1).get_nafn(), "D")
        self.assert_linked_list_order(linked_list, ["A"])
        self.assertEqual(linked_list.head.data.get_nafn(), "A")
        self.assertEqual(linked_list.head.next, None)
        self.assertEqual(linked_list.get_size(), 1)

        self.assertEqual(linked_list.pop(0).get_nafn(), "A")
        self.assertEqual(linked_list.head, None)
        self.assertEqual(linked_list.get_size(), 0)
        self.assertTrue(linked_list.is_empty())

        linked_list = create_test_data()

        self.assertEqual(linked_list.get_size(), 4)
        self.assertEqual(linked_list.pop(2).get_nafn(), "C")

        self.assert_linked_list_order(linked_list, ["A", "B", "D"])

        self.assertEqual(linked_list.pop(2).get_nafn(), "D")

        self.assert_linked_list_order(linked_list, ["A", "B"])


if __name__ == '__main__':
    unittest.main()
