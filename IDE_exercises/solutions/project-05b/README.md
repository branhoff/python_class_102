# project-5b

For this project, you will import the **json** module.

Write a class named NobelData that reads a [JSON file containing data on Nobel Prizes](http://api.nobelprize.org/v1/prize.json) and allows the user to search that data. It just needs to read a local JSON file - it doesn't need to access the internet. Specifically, your class should have an init method that reads the file, and it should have a method named search_nobel that takes as parameters a year and a category, and returns a sorted list (in normal English dictionary order) of the surnames for the winner(s) in that category for that year (up to three people can share the prize).  The year will be a string (e.g. "1975"), not a number.  The categories are: "chemistry", "economics", "literature", "peace", "physics", and "medicine".  The JSON file will be named **nobels.json** and will be provided - you do not need to submit it.  Any data members of the NobelData class must be **private**.

For example, your class could be used like this:
```
nd = NobelData()
nd.search_nobel("2001", "economics")
```

The file must be named: **NobelData.py**
