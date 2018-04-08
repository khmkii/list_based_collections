import unittest

from lbcollections import LinkedList


class LinkedListTests(unittest.TestCase):

    def setUp(self):
        self.fixture = [0,1,2,3,4,5]
        self.listy = LinkedList(self.fixture[1])

    def tearDown(self):
        del self.fixture
        del self.listy

    def test_get_position_returns_none_when_out_of_range(self):
        self.assertIsNone(self.listy.get_position(15))

    def test_get_position_raises_value_error_when_position_zero_or_less(self):
        self.assertRaises(ValueError, self.listy.get_position, 0)

    def test_get_position_raises_type_error_when_non_integer_supplied(self):
        self.assertRaises(TypeError, self.listy.get_position, 'a')

    def test_linked_list_get_position_returns_correctly(self):
        self.assertEqual(
            self.listy.get_position(1).value,
            self.fixture[1]
        )

    def test_linked_list_append(self):
        self.listy.append(self.fixture[2])
        self.assertEqual(
            self.listy.get_position(2).value,
            self.fixture[2]
        )

    def test_insert_at_root_position(self):
        self.listy.append(self.fixture[2])
        self.listy.insert(
            self.fixture[0],
            1
        )
        self.assertEqual(
            self.listy.get_position(1).value,
            self.fixture[0]
        )
        self.assertEqual(
            self.listy.get_position(2).value,
            self.fixture[1]
        )
        self.assertEqual(
            self.listy.get_position(3).value,
            self.fixture[2]
        )
        self.assertIsNone(self.listy.get_position(3).next)

    def test_insert_not_at_root_position(self):
        self.listy.append(self.fixture[3])
        self.listy.insert(
            self.fixture[2],
            2
        )
        self.assertEqual(
            self.listy.get_position(1).value,
            self.fixture[1]
        )
        self.assertEqual(
            self.listy.get_position(2).value,
            self.fixture[2]
        )
        self.assertEqual(
            self.listy.get_position(3).value,
            self.fixture[3]
        )
        self.assertIsNone(self.listy.get_position(3).next)

    def test_delete_at_root_position(self):
        self.listy.append(self.fixture[2])
        self.listy.append(self.fixture[3])
        self.listy.delete(1)
        self.assertEqual(
            self.listy.get_position(1).value,
            self.fixture[2]
        )
        self.assertEqual(
            self.listy.root_element,
            self.listy.get_position(1)
        )
        self.assertEqual(
            self.listy.get_position(2).value,
            self.fixture[3]
        )
        self.assertTrue(
            self.listy.root_element.root
        )

    def test_delete_other_than_root_position(self):
        self.listy.append(self.fixture[2])
        self.listy.append(self.fixture[3])
        self.listy.delete(2)
        self.assertIsNone(self.listy.get_position(3))
        self.assertEqual(
            self.listy.get_position(1).value,
            self.fixture[1]
        )
        self.assertEqual(
            self.listy.get_position(2).value,
            self.fixture[3]
        )
        self.assertEqual(
            self.listy.root_element,
            self.listy.get_position(1)
        )
        self.assertTrue(
            self.listy.root_element.root
        )

if __name__ == '__main__':
    unittest.main()
