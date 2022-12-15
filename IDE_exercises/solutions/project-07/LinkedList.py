 # Author: Brandon Hoffman
 # Date: 1/18/2021
 # Description: Represents LinkedList Object with recursion as the primary tool for LinkedList methods

class Node:
    """
    Represents a node in a linked list
    """
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        """
        gets Node data variable
        """
        return self.data

    def set_data(self, val):
        """
        sets Node data variable
        """
        self.data = val

    def get_next(self):
        """
        gets Node data variable
        """
        return self.next

    def set_next(self, val):
        """
        sets Node data variable
        """
        self.next = val

class LinkedList:
    """
    A linked list implementation of the List ADT
    """
    def __init__(self):
        self._head = None

    def get_head(self):
        """
        gets LinkedList head variable
        """

        return self._head

    def set_head(self, val):
        """
        sets LinkedList head variable
        """
        self._head = val

    def add(self, val):
        """
        Adds a node containing val to the linked list
        """
        self._head = self._add_helper(self._head, val)

    def _add_helper(self, a_node, val):
        """
        helper function for add func that adds a node containg val to the linked list
        """
        if a_node is None:
            return Node(val)

        else:
            a_node.next = self._add_helper(a_node.next, val)
            return a_node

    def insert(self, val, pos):
        """
        Adds a node contiang val to the linked list in position pos
        """
        self._head = self._insert_helper(self._head, val, pos)

    def _insert_helper(self, a_node, val, pos):
        """
        helper function for insert func adds a node containg val to the linked list in position pos
        """
        if a_node is None:
            return Node(val)

        if pos == 0:
            n = Node(val)
            n.next = a_node
            return n

        else:
            a_node.next = self._insert_helper(a_node.next, val, pos-1)
            return a_node

    def display(self):
        """
        Prints out the values in the linked list
        """
        self._display_helper(self._head)
        print()

    def _display_helper(self, a_node):
        """
        helper method for display method that prints out the values in the linked list
        """
        if a_node is None:
            return

        print(a_node.data, end=" ")
        self._display_helper(a_node.next)
        

    def remove(self, val):
        """
        Removes the node containing val from the linked list
        """
        self._head = self._remove_helper(self._head, val)

    def _remove_helper(self, a_node, val):
        """
        helper function for remove func to Removes the node containing val from the linked list
        """
        if a_node is None:
            return a_node
        elif a_node.data == val:
            return a_node.next

        else:
            a_node.next = self._remove_helper(a_node.next, val)
            return a_node

    def contains(self, val):
        """
        returns True if value exists in LinkedList
        else returns False
        """
        return self._contains_helper(self._head, val)

    def _contains_helper(self, a_node, val):
        """
        helpe function for contains method
        returns True if value exists in LinkedList
        else returns False
        """
        if a_node is None:
            return False

        if a_node.data == val:
            return True

        return self._contains_helper(a_node.next, val)


    def is_empty(self):
        """
        Returns True if the linked list is empty,
        returns False otherwise
        """
        return self._head is None

    def reverse(self):
        """
        reverses LinkedList by rearrange the order of the nodes in the LinkedList
        """
        self._head = self._reverse_helper(self._head)

    def _reverse_helper(self, a_node):
        """
        helper method for reverse method
        reverses LinkedList by rearrange the order of the nodes in the LinkedList
        """
        if a_node is None or  a_node.next is None:
            return a_node

        next_node = a_node.next
        remaining = self._reverse_helper(a_node.next)
        next_node.next = a_node
        a_node.next = None
        return remaining
        
    def to_plain_list(self):
        """
        Returns a regular Python list containing the same values, in the same order, as the linked list
        """
        result = []
        self._to_plain_list_helper(self._head, result)
        return result

    def _to_plain_list_helper(self, a_node, result):
        """
        helper method for to_plain_list method that Returns a regular Python list containing the same values, in the same order, as the linked list
        """
        if a_node is None:
            return result
        result.append(a_node.data)
        return self._to_plain_list_helper(a_node.next, result)
