# nyc-property-sales
BigData - 44517


Project Number - 3


<b>Team Members:</b>
  - Lahari Thamatam
  - Vijaya Raja Mayuri
  - Sneha Ojha
  
  # Links
  Repository Link:  (https://github.com/Thamatamlahari/nyc-property-sales)
  
  Issuetracker Link:   (https://github.com/Thamatamlahari/nyc-property-sales/issues)
  
  
 # Introduction
 
 
 This dataset is a record of every building or building unit (apartment, etc.) sold in the New York City property market over a 12-month period.
 
 # Data Source
 
- The data is in csv format.
- The key attributes are year built, residential units, commercial units, total units.
- Volume: The data size is 13MB. It consists of 84548 rows and 22 columns. There is one data source. The data  was updated 2 years ago.
- Variety: The data is structured. The data set is in excel form.
- Velocity: Velocity of the data set is zero as it was updated 2 years ago.
- Veracity: The data is structured and cleaned and it is not messy. The data is trustworthy.
- Value: The property dealers can use this. They can find the future trends using this data.

Link for the Data source:   


https://www.kaggle.com/new-york-city/nyc-property-sales#nyc-rolling-sales.csv

# BigData Problems

for year built i will find the sum of residential units listed.

Mapper input: 1 ALPHABET CITY 07 RENTALS - WALKUP APARTMENTS             2A 392 6 C2 153 AVENUE B 10009 5 0 5 1633 6440 1900 2 C2 6625000 7/19/2017 0:00

Mapper output: 1920 10
Reducer output:1920 300
Chart type: Bar Chart
---lahari 
for year built i will find the maximum of residential units listed.
Mapper input: 1 ALPHABET CITY 07 RENTALS - WALKUP APARTMENTS             2A 392 6 C2 153 AVENUE B 10009 5 0 5 1633 6440 1900 2 C2 6625000 7/19/2017 0:00

Mapper output: 1920 10
Reducer output:1920 70
Chart type: Bar Chart
---Mayuri
for year built i will find the count of residential units listed.
Mapper input: 1 ALPHABET CITY 07 RENTALS - WALKUP APARTMENTS             2A 392 6 C2 153 AVENUE B 10009 5 0 5 1633 6440 1900 2 C2 6625000 7/19/2017 0:00

Mapper output: 1920 1
Reducer output:1920 80000
Chart type: Bar Chart
---Sneha


