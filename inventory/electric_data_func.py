import requests

API_KEY = '37ff344278e478d96077a269fe0966d4'

# Create function to scrape EIA Data
def eiaScrape(BA, API_KEY):

    ''' Function will collect data from EIA website at hourly intervals.
        Must have EIA API Key from EIA website and specify the Balancing Authority (BA).
        BA abbreviation must match abbreviations found here https://www.eia.gov/opendata/qb.php?category=2122628  '''

    url = f'http://api.eia.gov/series/?api_key={API_KEY}&series_id=EBA.{BA}-ALL.D.HL'

    data = requests.get(url=url).json()

    data = pd.DataFrame(data.get('series')[0].get('data'), columns=['Date', 'Load'])

    data['Date'] = pd.to_datetime(dat['Date'])

    return data
