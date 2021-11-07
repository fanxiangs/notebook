import unittest

from Python.data_structures.linked_list.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_append(self):
        linked_list = LinkedList()
        linked_list.append(10)
        linked_list.append('a')
        self.assertEqual(linked_list.get_all_data(), [10, 'a'])

    def test_add_first(self):
        linked_list = LinkedList()
        linked_list.append(10)
        linked_list.add_first(1)
        self.assertEqual(linked_list.get_all_data(), [1, 10])

    def test_insert(self):
        linked_list = LinkedList()
        linked_list.append(10)
        linked_list.insert(0, 9)
        self.assertEqual(linked_list.get_all_data(), [9, 10])
        linked_list.insert(-2, 8)
        self.assertEqual(linked_list.get_all_data(), [8, 9, 10])
        linked_list.insert(6, 11)
        self.assertEqual(linked_list.get_all_data(), [8, 9, 10, 11])

    def test_delete(self):
        linked_list = LinkedList()
        linked_list.append(10)
        linked_list.append(11)
        linked_list.append(12)
        linked_list.append(13)
        self.assertEqual(linked_list.get_all_data(), [10, 11, 12, 13])
        linked_list.delete(12)
        self.assertEqual(linked_list.get_all_data(), [10, 11, 13])


if __name__ == '__main__':
    unittest.main()
