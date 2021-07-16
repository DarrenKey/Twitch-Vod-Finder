import requests
import os
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv('client_id')
print(client_id)
