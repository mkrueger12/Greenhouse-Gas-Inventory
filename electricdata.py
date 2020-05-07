from inventory import config
import requests

API_KEY = '37ff344278e478d96077a269fe0966d4'

# Create function to scrape EIA Data
def eiaScrape(API_KEY):

    ''' Function will collect data from EIA website at hourly intervals.
        Must have EIA API Key from EIA website and specify the Balancing Authority (BA).
        Currently only supports collecting data from PSCO. '''

    url = f'http://api.eia.gov/series/?api_key={API_KEY}&series_id=EBA.PSCO-ALL.D.HL'

    data = requests.get(url=url).json()

    return data