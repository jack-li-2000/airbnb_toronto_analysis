# airbnb_toronto_analysis
 An analysis of airbnb in Toronto. Includes data cleaning and combining in python and visualizations in tableau.
![image](https://github.com/jack-li-2000/airbnb_toronto_analysis/assets/59067741/e9177f88-af6a-41c7-bcc8-2581b181d13f)

average price by neighborhood 
![image](https://github.com/jack-li-2000/airbnb_toronto_analysis/assets/59067741/b3598d14-9f04-4ee1-9b36-b9e39e968f6f)

The dataframes used in this visualization contained too many rows and cannot be uploaded to tableau public. Please unzip the files listings.csv, reviews.csv, calendar.csv and point to them in tableau to view the visualization. Alternatively, use the twbx file.

In the python data processing, three files are merged: listings.csv, reviews.csv, calendar.csv. Listings dataframe has 1 row per listing_ID, this is the unique id for one airbnb from the owner, this unique listing can be booked by people over time which results in multiple entries for this unique listing ID in reviews (multiple people give reviews for the airbnb) and calendar (different people book on different dates) dataframes.

Using a custom function, the review and calendar entries for the same listing_ID are converted into lists and are flattened into 1 row per unique listing ID, then are merged with listing ID. The resulting dataframe is a 3 dimensional dataframe with each unique listing ID taking 1 row. 

A similar result is achieved using Tableau's built in data frame join methods for visualization. 
