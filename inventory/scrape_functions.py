import requests
import pandas as pd
import datetime as dt

# Create function to scrape EIA Data
def eiaNetGen(BA, API_KEY, SOURCE):

    """ Function will collect net generation data from EIA website at hourly intervals.
        Must have EIA API Key from EIA website and specify the Balancing Authority (BA).
        BA abbreviation must match abbreviations found here:
        https://www.eia.gov/opendata/qb.php?category=2122628.
        Source Options include solar (SUN), wind (WND), coal (COL),
        hydro (WAT), nat gas (NG), petroleum (OIL), or total net gen (ALL).
        Returns most recent 36 hours. """

    if SOURCE == 'ALL':
        url = f'http://api.eia.gov/series/?api_key={API_KEY}&series_id=EBA.{BA}-ALL.NG.HL'
    else:
        url = f'http://api.eia.gov/series/?api_key={API_KEY}&series_id=EBA.{BA}-ALL.NG.{SOURCE}.HL'

    data = requests.get(url=url).json()

    data = pd.DataFrame(data.get('series')[0].get('data'), columns=['Date', 'Load'])

    data['Date'] = pd.to_datetime(data['Date'])

    data['Date'] = data['Date'].apply(lambda x: dt.datetime.strftime(x, '%Y%m%d%H%M'))

    data['src'] = SOURCE

    data['ba'] = BA

    data = data.head(73)

    data = data.tail(72)

    return data
