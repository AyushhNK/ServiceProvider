import requests
def get_city_name(latitude, longitude, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        city = data.get('name')
        if city:
            return city
        else:
            return "City not found"
    else:
        return f"Error: {data.get('message', 'API request failed')}"
