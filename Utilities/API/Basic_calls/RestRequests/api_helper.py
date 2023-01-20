import requests
import json


class api_helper :
    
    def set_url (base_url, url ):
        url = base_url + url
        return url
    
    