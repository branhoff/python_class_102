


import unittest
from LinkedList import Node, LinkedList

class LinkedListTester(unittest.TestCase):
    """

    """

    def test_linked_list(self):
        """

        """

        linked_list = LinkedList()

        linked_list.add(6)
        linked_list.add(8)
        linked_list.add(47)
        linked_list.add(-1)
        
        linked_list.display()


if __name__ == '__main__':
    unittest.main()