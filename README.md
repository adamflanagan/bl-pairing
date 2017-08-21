The goal is to build a working implementation using the provided sample file. Code does not need to be production ready, however correct behaviour should be demonstrable.

### Background
Bricklane wants to gather data on the property market to help inform where to buy properties. One of the data points we can use is the Land Registry transaction data. This is a record of every house sale since 1995. Every month a new file is published which contains new, amended and deleted transactions.

pp-monthly-update-sample.csv contains a subset of the changes for July 2017.
An explanation of the column headers can be found here: https://www.gov.uk/guidance/about-the-price-paid-data#explanations-of-column-headers-in-the-ppd

### Exercise
Write a script to clean the data and split it into two files. properties.csv and transactions.csv.
* Rows in transactions.csv should reference a row in properties.csv
* Data should be cleaned and human readable.
* There should be no duplicates.
