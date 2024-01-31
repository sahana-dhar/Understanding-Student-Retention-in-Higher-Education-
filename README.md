# Understanding Student Retention in Higher Education
## Objective
Our primary objective is to examine the factors influencing a college or university's retention rates. This can provide valuable insights into what college freshmen are hoping for when entering higher education and help institutions better meet the needs of their student body.

We want to answer the questions:
- Which aspects are most strongly associated with a high retention rate?​
- How do various institutional factors impact the likelihood of freshmen returning for their sophomore year?

## Data Description
#### Web Scraping
We used [A-Z List of Colleges](https://www.4icu.org/us/a-z/), taking the first column of the table on this site to create our list of colleges in the United States that we wanted to use in our dataset.
#### College API
In order to get the information on retention rates and target features for each college, we used the [College Scorecard API](https://collegescorecard.ed.gov/data/documentation/), a GET API that returns data for every college in a dictionary.
#### Cleaning the Data
Our dataset was scaled, to ensure that our data was standardized (ex: SAT vs Retention rate are completely different scales) and all NaN rows were dropped. This left us with 794 rows and 9 columns.​

## Visualizing the Data
