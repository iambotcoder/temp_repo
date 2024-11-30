import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT = os.environ["SHEETY_PRICES_ENDPOINT"]
SHEETY_USERS_ENDPOINT = os.environ["SHEETY_USERS_ENDPOINT"]

class DataManager:

    def __init__(self):
        self._user = os.environ["SHEETY_USRERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.SHEETY_PRICES_ENDPOINT =  os.environ["SHEETY_PRICES_ENDPOINT"]
        self.SHEETY_USERS_ENDPOINT = os.environ["SHEETY_USERS_ENDPOINT"]
        self.destination_data = {}
        self.user_data = {}
    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=self.SHEETY_PRICES_ENDPOINT)
        data = response.json()
        print(data)
        self.destination_data = data["prices"]
        # Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=self.SHEETY_USERS_ENDPOINT)
        data = response.json()
        print(data)
        self.user_data = data["users"]
        # Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.user_data
