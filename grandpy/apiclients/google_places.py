"""Connection manager module.
"""
import requests

from configuration.config import Config, LOCATION_BIAS


class GooglePlaces:
    """
    """
    def __init__(self, parsed_string):
        self.config = Config()
        self.endpoint = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"
        self.parameters = {
                "input" : parsed_string,
                "inputtype" : "textquery",
                "fields": "place_id,name,formatted_address",
                "locationbias": "rectangle:48.7731,2.3056|48.7918,2.3307", #LOCATION_BIAS,
                "key" : self.config.GG_API_KEY
                }
        self.places_api_answer = None
        self.place_id = ""
        self.name = ""
        self.address = ""

    def get_places(self):
        """
        """
        try:
            response_api = requests.get(self.endpoint, params = self.parameters)
            self.places_api_answer = response_api.json()
        except requests.ConnectionError as error:
            print(error.value)
            # print(
            #     "Un problème de connection est apparu. Ré-essaayez plus"
            #     " tard ou contacter le propriétaire de l'application")
        except requests.Timeout:
            print(
                "Un problème de connection est apparu. Ré-essaayez plus"
                " tard ou contacter le propriétaire de l'application")

    def set_attribute(self):
        """
        """ 
        candidates = self.places_api_answer["candidates"]
        for candidate in candidates:
            self.place_id = candidate["place_id"]
            self.name = candidate["name"]
            self.address = candidate["formatted_address"]

        if len(candidates) == 0:
            self.address = "Desolé je ne reconnais pas cet endroit"
