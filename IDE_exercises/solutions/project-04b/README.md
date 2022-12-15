# project-4b

Write a Box class whose init method takes three parameters and uses them to initialize the **private** length, width and height data members of a Box.  It should also have a method named **volume** that returns the volume of the Box.  It should have get methods named get_length, get_width, and get_height.

Write a separate function named box_sort (not part of the Box class) that uses insertion sort to sort a list of Boxes from greatest volume to least volume.

For example, they could be used like this:
```
b1 = Box(3.4, 19.8, 2.1)
b2 = Box(1.0, 1.0, 1.0)
b3 = Box(8.2, 8.2, 4.5)
box_list = [b1, b2, b3]
box_sort(box_list)
```

The file must be named: **box_sort.py**
