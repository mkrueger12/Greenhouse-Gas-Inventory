from inventory.scrape_functions import eiaNetGen
from inventory.config import EIA_API_KEY

BA = 'PSCO'
API_KEY = EIA_API_KEY

# Collect Data
solar = eiaNetGen(BA, API_KEY, 'SUN')
wind = eiaNetGen(BA, API_KEY, 'WND')
all = eiaNetGen(BA, API_KEY, 'ALL')
