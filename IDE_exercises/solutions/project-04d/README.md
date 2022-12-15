# project-4d

Write a bubble sort that counts the number of comparisons and the number of exchanges made while sorting a list and returns a tuple of the two values (comparisons first, exchanges second).  Do the same for insertion sort.  Name these functions **bubble_count** and **insertion_count**.  Your functions should **only** count comparisons between the values that are being sorted.

Try sorting various lists with both functions.  What do you notice about the number of comparisons and exchanges made for lists of different sizes?  What do you notice for lists that are nearly sorted vs. lists that are nearly reversed?  You don't need to submit your observations, just the functions.

Hint 1: For insertion sort, every time the value (that is currently getting "inserted" to its correct place) shifts one position to the left counts as an exchange.  Watching the visualization for insertion sort may help make that more intuitive.

Hint 2: For insertion sort, if we assume that we've already finished sorting all but the last value, then finding the right place for the 3 in [2, 4, 6, **3**] and finding the right place for the 1 in [2, 4, 6, **1**] would both take three comparisons, because in both cases the number being placed is compared to 6, then 4, then 2.

The file must be named: **sorts_count.py**
