# project-07

Write a LinkedList class that has **recursive** implementations of the `add` and `remove` methods described in the Exploration.  It should also have **recursive** implementations of the `contains`, `insert`, and `reverse` methods described in the exercises.  The reverse method should **not** change the _data_ value each node holds - it must rearrange the order of the nodes in the linked list (by changing the _next_ value each node holds).

It should have a **recursive** method named `to_plain_list` that takes no parameters and returns a regular Python list that has the same values (from the `data` attribute of the Node objects), in the same order, as the current state of the linked list.

It should have a method named `get_head` that takes no parameters and returns the Node object (_not_ the value inside it) that is at the `_head` of the linked list.

The `head` data member of the LinkedList class, as well as the `data` and `next` members for the Node class must be private and have getters and setters defined.

All the methods should have the arguments in the same order as you saw in the Lesson. You may use default arguments and/or helper functions. 

Your recursive functions must **not**:
* use any loops
* use any variables declared outside of the function
* use any mutable default arguments

Here's an example of how a recursive version of the display() method from the lesson could be written:
```
    def rec_display(self, a_node):
        """recursive display method"""
        if a_node is None:
            return
        print(a_node.get_data(), end=" ")
        self.rec_display(a_node.get_next())

    def display(self):
        """recursive display helper method"""
        self.rec_display(self.get_head())
```

All your classes must be in a single file named: **LinkedList.py**
