
import requests, json
from .models import Quote

url = "http://quotes.stormconsultancy.co.uk/random.json"

def get_quotes():
    """
    Function to consume http request and return a Quote class instance
    """
    response = requests.get(url).json()

    random_quote = Quote(response.get("id"),response.get("author"),response.get("quote"), response.get("permalink"))
    return random_quote