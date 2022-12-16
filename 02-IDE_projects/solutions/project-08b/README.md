# project-08b

For this project, you will import the **time** and **random** modules.  You will also install the **matplotlib** package and import from it the **pyplot** module.  You will also import the wraps() function from the functools module for use in your decorator.

Use the **time** module to write a decorator function named sort_timer that times how many seconds it takes the decorated function to run.  Since sort functions don't need to return anything, have the decorator's wrapper function return that elapsed time.

To get the current time, call time.perf_counter().  Subtracting the begin time from the end time will give you the elapsed time in seconds.

Copy the code for bubble sort and insertion sort from Module 4 and decorate them with sort_timer.

Write a function called **compare_sorts** that takes the two decorated sort functions as parameters.  It should randomly generate a list of 1000 numbers and then make a separate copy of that list, which you can do like this:
```
list_2 = list(list_1)
```
Next it should time how long it takes bubble sort to sort one of those copies (using the decorated bubble sort), and then time how long it takes insertion sort to sort the other copy (using the decorated insertion sort).  This gets us the first data point for each algorithm.  The function should now repeat this for lists of size 2000, 3000, and so on, up to 10000.  For each list size, the function should randomly generate a list of that size and time how long it takes each algorithm to sort it.  The random numbers should all be integers in the range 1 <= r <= 10000.  Once the function has the 10 time data points for each algorithm, it will generate a graph comparing them.

To generate random numbers, you will need to import the **random** module.  The function call random.randint(a, b) returns a random integer N such that a <= N <= b.  You should use a = 1 and b = 10000.  It's fine if values appear in the list multiple times.

To generate a graph, you will need to install the **matplotlib** package and import **pyplot** from it.  Below is an example of code to produce a graph comparing two series of data points - **you will need to modify it to graph your timing data**.
```
from matplotlib import pyplot
pyplot.plot([1, 2, 3, 4, 10], [1, 4, 9, 16, 100], 'ro--', linewidth=2)
pyplot.plot([1, 2, 3, 4, 10], [1, 3, 7, 20, 150], 'go--', linewidth=2)
pyplot.xlabel("the x label")
pyplot.ylabel("the y label")
pyplot.show()
```
Each of the calls to the plot function plot a line.  The call to the show function displays the graph.  In the calls to the plot function, the first list is the list of x-coordinates (which is the same list for both curves you're plotting).  The second list is the list of y-coordinates.  The 'ro--' tells it to use red circles connected by a dashed line and 'go--' is the same except green instead of red.  The linewidth parameter is self-explanatory.  The xlabel and ylabel parameters set the labels for the x and y axes. For your graph, the x axis is the number of elements being sorted, and the y axis is the time in seconds.

You'll still submit this project in Gradescope, but Gradescope won't run any tests - the TAs will take care of that.

(Keep in mind that the time it takes an algorithm to sort a list depends on the list, so if you wanted your graph to be more robust, you would randomly generate say 100 different lists of each length and average their sort times together to get each data point.  However, that would take significantly longer to run, and therefore for the TAs to grade, so for this assignment, stick to one list of each size.)

Because Gradescope will not be testing this project, you should include a line that calls your compare_sorts() function to generate the graph - just to make things a little more efficient for the TAs.

Your file must be named: **sort_timer.py**

