# project-1

For this project, you will import the **statistics** module.

Write a class called Person that has two **private** data members - the person's name and age.  It should have an init method that takes two values and uses them to initialize the data members.  It should have a get_age method.

Write a separate function (not part of the Person class) called basic_stats that takes as a parameter a list of Person objects and returns a tuple containing the mean, median, and mode of all the ages.  To do this, use the mean, median and mode functions in the statistics module.  Your basic_stats function should return those three values as a tuple, in the order given above.

For example, it could be used as follows:
```
p1 = Person("Kyoungmin", 73)
p2 = Person("Mercedes", 24)
p3 = Person("Avanika", 48)
p4 = Person("Marta", 24)

person_list = [p1, p2, p3, p4]
print(basic_stats(person_list))  # should print a tuple of three values
```

Mini-review: A private data member of a class has a name that begins with an underscore.  Private data members can be directly accessed from within the class, but **not** from outside the class.  Instead, if a data member needs to be accessed or manipulated from outside the class, then the class should provide a method that can be called to carry out the necessary actions.  This access restriction is not enforced by the Python language as it is in some other languages, due to the Python philosophy of "we're all adults here".

The file must be named: **basic_stats.py**
