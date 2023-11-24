API_URL = 'http://localhost:8080/api/v2/'


class WeatherService():
# BEGIN (write your solution here)

    def __init__(self, http_client):
        self.client = http_client

    def look_up(self, city):
        get_ = self.client.get(f'{API_URL}cities/{city}', )
        info = get_.json()
        return info

# END
