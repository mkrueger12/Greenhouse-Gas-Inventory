import requests
import pandas as pd
from inventory.scrape_functions import eiaNetGen

BA = 'PSCO'
API_KEY = EIA_API_KEY

# Collect Data
solar = eiaNetGen(BA, API_KEY, 'SUN')
wind = eiaNetGen(BA, API_KEY, 'WND')