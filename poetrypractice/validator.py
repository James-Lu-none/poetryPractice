import requests
class PhoneNumberValidator:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.api_url = "https://api.numlookupapi.com/v1/validate/"

    def validate(self, phone_number: str, country_code: str = None) -> bool:
        if not phone_number:
            raise ValueError("Phone Number cannot be empty!")
        
        response = self.__make_api_call(phone_number, country_code)
        if response.ok:
            return response.json()["valid"]
        else:
            response.raise_for_status()

    # make_api_call is a semi_private method, so we need to add __ to it, if only add one _,
    # it only signaling to other developers that these members are not part of the public 
    # interface and should be used with caution.
    def __make_api_call(self, phone_number: str, country_code: str = None):
        params = {"apikey": self.api_key}
        if country_code:
            params["country_code"] = country_code
        response = requests.get(self.api_url + phone_number, params=params)
        return response