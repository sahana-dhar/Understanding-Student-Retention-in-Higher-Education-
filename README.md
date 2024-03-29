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
<img width="584" alt="Retention Rate vs  Various Features" src="https://github.com/sahana-dhar/Understanding-Student-Retention-in-Higher-Education-/assets/113061193/0f9b18f9-2ead-469b-970a-5dd1b139bbf1">
From this preliminary visualization, we can tell that stronger relationships exist between retention rate and SAT scores, earnings 6 years after entry, faculty salary, and the share of first-generation students. We can also see weaker relationships exist between retention rate and acceptance rate, student-faculty ratio, mean net price, diversity, and amount of students with loans. 

## Machine Learning Methods
### Random Forest Regressor
- Predict numerical target variable with multiple features​
- Analyze feature importance​
- More complex than Linear Regression
#### Results:
<img width="400" alt="RFR feature importance" src="https://github.com/sahana-dhar/Understanding-Student-Retention-in-Higher-Education-/assets/113061193/16b56599-856b-42e0-a74b-bcab2437359b">
<img width="700" alt="RFR feature scatter plots" src="https://github.com/sahana-dhar/Understanding-Student-Retention-in-Higher-Education-/assets/113061193/440fb5c1-b03b-4174-9c5b-c23bee29561b">

Based on the RFR feature importance results, SAT scores, faculty salary, and earnings 6 years after entry contributed most to the retention rate. An RFR model with only those features returned these results when predicting retention rate:

- Mean Squared Error: 0.0051
- $R^2$: 0.6012
- Mean Absolute Error: 0.0491
- Good balance between a high $R^2$ and low $MSEs$ and $MAEs$
- Not overly complicated with too many features

### Linear Regression
- Predict numerical target variable with multiple features​
- Best suited for data with linear relationships​
- Simple, easy to interpret ​
#### Results:
<img width="618" alt="linear regression feature importance" src="https://github.com/sahana-dhar/Understanding-Student-Retention-in-Higher-Education-/assets/113061193/20d1e1b5-8841-4e9c-bce9-21cf447634c6">
<img width="821" alt="linear regression scatter plots" src="https://github.com/sahana-dhar/Understanding-Student-Retention-in-Higher-Education-/assets/113061193/15a3bcef-a4cf-40a5-ad01-3b4427cbd95f">

Based on the Linear Regression feature importance results, SAT scores, share of first-generation students, and faculty salary contribute most to the retention rate. A Linear Regression model with only those features returned these results when predicting retention rate:

- Mean Squared Error: 0.0043​
- $R^2$: 0.6599​
- Mean Absolute Error: 0.0494​
- ​Low $MSE$ and $MAE$ values suggest a minimal difference between actual and predicted observations for retention rate
- Top 3 predictor variables account for 66% of the variance in the target variable (retention rate)

## Conclusions
#### Initiatives for first-generation students
- Aiding first-generation students with college applications as their families are more unfamiliar with the process​
- Offering on-campus resources to help first-gen students feel more welcome and smoothen their transition to college​
#### Improve faculty salary and benefits
- Creating a comprehensive step-salary structure that factors in tenure, expertise, market data, geography, and performance  ​
- Providing a clear path for promotion, raises, and ample benefits​
#### Bolster campus culture
- Combatting student unsatisfaction with proper feedback mechanisms: ​
  - Tutoring services​
  - Mental health and physical wellness support​
  - Guidance counseling and career conferences​
### Limitations and next steps
- After dropping null values, there were only 794 colleges in the data set​
- Retention rate is related to but doesn't fully encapsulate freshman satisfaction​
- Working with a larger number of observations could improve predictive power​
- Different features, both predictor and target, may more accurately answer the key questions​

​

​
