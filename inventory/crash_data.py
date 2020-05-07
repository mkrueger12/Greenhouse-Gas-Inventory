# This script is used to scrape daily crash data from the City and County of Denver. This can be used to aproximate 
# vehicle mile traveled (VMT) within city limits.

import pandas as pd
import datetime as dt
import numpy

#Scrape Data
url = 'https://www.denvergov.org/media/gis/DataCatalog/traffic_accidents/csv/traffic_accidents.csv'
data = pd.read_csv(url)
print('Data Aquired')

#Clean Data
data = data[['INCIDENT_ID', 'REPORTED_DATE']]
data['Year'] = pd.to_datetime(data['REPORTED_DATE'])
data['Year'] = data['Year'].dt.year
data = data[['INCIDENT_ID', 'Year']]
print('Data Cleaned')

#Group By and Count
data_grouped = data.groupby('Year')
data_grouped = data_grouped.count()
print('Data Grouped')

#Write to CSV
data_grouped.to_csv(#Insert file path)
print('Complete')

