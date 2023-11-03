#!/usr/bin/env python
# coding: utf-8

# In[128]:


import requests

api_key = 'fK3eae9BKJ8nZKxDTxtAPEXjfi02c3oAhK5aPCdx'

base_url = 'http://api.data.gov/ed/collegescorecard/v1/schools'

colleges = [
    'Harvard',
]

for college_name in colleges:
    params = {
        'api_key': api_key,
        'school.name': college_name,
    }

response = requests.get(base_url, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f'API request failed with status code: {response.status_code}')

    


# In[140]:


import requests
import pandas as pd

api_key = 'fK3eae9BKJ8nZKxDTxtAPEXjfi02c3oAhK5aPCdx'
base_url = 'http://api.data.gov/ed/collegescorecard/v1/schools'

colleges = ['Harvard', 'Stanford', 'Columbia']

# Initialize an empty DataFrame
result_df = pd.DataFrame(columns=['College', 'SAT', 'Earnings 6 yrs after entry', 'Share First Generation', 'Retention'])

for college_name in colleges:
    params = {
        'api_key': api_key,
        'school.name': college_name,
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()

        # Extract the desired data
        try:
            sat_score = data['results'][0]['latest']['admissions']['sat_scores']['average']['overall']
            earnings = data['results'][0]['latest']['earnings']['6_yrs_after_entry']['median']
            first_gen_percentage = data['results'][0]['latest']['student']['share_firstgeneration']
            retention = data['results'][0]['latest']['student']['retention_rate']['overall']['full_time']

            # Create a DataFrame for the current college
            data_dict = {
                'College': [college_name],
                'SAT': [sat_score],
                'Earnings 6 yrs after entry': [earnings],
                'Share First Generation': [first_gen_percentage],
                'Retention': [retention]
            }

            college_df = pd.DataFrame(data_dict)

            # Concatenate the college DataFrame to the result_df
            result_df = pd.concat([result_df, college_df], ignore_index=True)
        except (KeyError, IndexError):
            print(f"Data not found for {college_name}")
    else:
        print(f'API request failed with status code: {response.status_code} for {college_name}')

# Print the resulting DataFrame
result_df.head()

