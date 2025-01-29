import os
from dotenv import load_dotenv
import requests


load_dotenv()

API_KEY_ID= os.getenv('API_KEY_ID')
API_KEY_SECRET= os.getenv('API_KEY_SECRET')

response = requests.get(url='https://www.apsis.com')

print(response.text)