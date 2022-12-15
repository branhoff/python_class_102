# project-5c

For this project, you will import the **json** module.

Write a class named SatData that reads a [JSON file containing data on 2010 SAT results for New York City](https://data.cityofnewyork.us/api/views/zt9s-n5aj/rows.json?accessType=DOWNLOAD) and writes the data to a text file in CSV format (CSV is a vendor-neutral format for spreadsheets, which uses commas to separate values). Your class just needs to read a local JSON file - it doesn't need to access the internet. Specifically, your class should have an init method that reads the file, and it should have a method named **save_as_csv** that takes as a parameter a list of DBNs (district bureau numbers) and saves a CSV file that looks like [this](https://data.cityofnewyork.us/api/views/zt9s-n5aj/rows.csv?accessType=DOWNLOAD), but with only the rows corresponding to the DBNs in the list (and also the row of column headers). **Open the file as a text file rather than as a spreadsheet, so that you can see the CSV syntax.** You may assume that all of the DBNs in the list passed to your method are all present in the JSON file.  The rows in the CSV file must be sorted in ascending order by DBN.  The name of the file must be **output.csv**.  There is a csv module for Python, but you will not use it for this project.  CSV is a very simple format - just commas separating columns and newlines separating rows (see note below about commas in field names).  The JSON file will be named **sat.json** and will be provided - you do not need to submit it.  Any data members of the SatData class must be **private**.

For example, your class could be used like this:
```
sd = SatData()
dbns = ["02M303", "02M294", "01M450", "02M418"]
sd.save_as_csv(dbns)
```

You may hardcode the column headers.

Some of the school names contain one or more commas. How should you preserve such a name as a single field in CSV format, since commas normally separate fields? The correct way to handle that is to enclose such names in double quotes in your CSV file.  If you open up the example CSV file in a text editor, you can see that's what it does.

The file must be named: **SatData.py**
