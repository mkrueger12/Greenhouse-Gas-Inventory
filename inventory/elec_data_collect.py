from inventory.scrape_functions import eiaNetGen
from inventory.config import EIA_API_KEY

BA = 'PSCO'
API_KEY = EIA_API_KEY

# Collect Data
solar = eiaNetGen(BA, API_KEY, 'SUN')
wind = eiaNetGen(BA, API_KEY, 'WND')
col = eiaNetGen(BA, API_KEY, 'COL')
hydro = eiaNetGen(BA, API_KEY, 'WAT')
natgas = eiaNetGen(BA, API_KEY, 'NG')
petrol = eiaNetGen(BA, API_KEY, 'OIL')
all = eiaNetGen(BA, API_KEY, 'ALL')

# Append Data


