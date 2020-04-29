# This script is used to scrape daily crash data from the City and County of Denver. This can be used to aproximate 
# vehicle mile traveled (VMT) within city limits.


import pandas as pd
import datetime as dt
import numpy


#Scrape Data
#url = 'https://services1.arcgis.com/zdB7qR0BtYrg0Xpl/ArcGIS/rest/services/ODC_CRIME_TRAFFICACCIDENTS_P/FeatureServer/239/query?where=OBJECTID++%3E+0&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&returnGeodetic=false&outFields=INCIDENT_ID%2C+REPORTED_DATE&returnGeometry=false&featureEncoding=esriDefault&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnQueryGeometry=false&returnDistinctValues=false&cacheHint=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&returnExceededLimitFeatures=false&quantizationParameters=&sqlFormat=none&f=pjson&token='
#crash = requests.get(url).json()
url = 'https://www.denvergov.org/media/gis/DataCatalog/traffic_accidents/csv/traffic_accidents.csv'
data = pd.read_csv(url)
print("Data Aquired")


#Clean Data
data = data[['INCIDENT_ID', 'REPORTED_DATE']]
data['Year'] = pd.to_datetime(data['REPORTED_DATE'])
data['Year'] = data['Year'].dt.year
data = data[['INCIDENT_ID', 'Year']]
print("Data Cleaned")

#Group By and Count
data_grouped = data.groupby('Year')
data_grouped = data_grouped.count()
print("Data Grouped")

#Write to CSV
data_grouped.to_csv(r'C:\Users\max\OneDrive\Documents\Python\Denver GHG\Data\annual_accidents.csv')
print("Complete")

