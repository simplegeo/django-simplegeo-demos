from _version import __version__

API_VERSION = '1.0'

from httplib2 import Http
import oauth2 as oauth
from urlparse import urljoin
import time

# example: http://api.simplegeo.com/0.1/context/37.797476,-122.424082.json

from simplegeo.shared import Client, APIError, DecodeError, json_decode

class ContextClient(Client):
    def __init__(self, key, secret, api_version=API_VERSION, host="api.simplegeo.com", port=80):
        Client.__init__(self, key, secret, api_version=api_version, host=host, port=port)

        self.endpoints['context'] = 'context/%(lat)s,%(lon)s.json'

    def get_context(self, lat, lon):
        endpoint = self.endpoint('context', lat=lat, lon=lon)
        return json_decode(self._request(endpoint, "GET"))
