import requests

# Create function to scrape EIA Data
def eiaScrape(BA, API_KEY):

    ''' Function will collect data from EIA website at hourly intervals.
        Must have EIA API Key from EIA website and specify the Balancing Authority (BA).
         BA must be the BA abbreviation found here https://www.eia.gov/opendata/qb.php?category=2122628 '''

    url = f'http://api.eia.gov/series/?api_key={API_KEY}&series_id=EBA.{BA}-ALL.D.HL'

    data = requests.get(url=url).json()

    return data
