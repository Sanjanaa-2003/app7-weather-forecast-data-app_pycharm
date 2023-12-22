import requests

API_KEY = "7f08eea83d936e300c3ba1dc9c7ffd7a"

def get_data(place, forecast_days=None, kind=None):
    url=f"http://api.openweathermap.org/data/2.5/forecast?id=3163858&appid={API_KEY}"
    # url=f"http://api.openweathermap.org/data/2.5/forecast?id={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_values = 8* forecast_days
    filtered_data = filtered_data[:nr_values]
    if kind == 'Temperature':
        filtered_data=[dict["main"]["temp"] for dict in filtered_data]
    if kind == 'Sky':
        filtered_data=[dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data
    # "http://api.openweathermap.org/data/2.5/forecast?id=3163858&appid=7f08eea83d936e300c3ba1dc9c7ffd7a

if __name__ == "__main__":
    print(get_data(place="Tokyo",forecast_days=3,kind="Temperature"))

# http://api.openweathermap.org/data/2.5/forecast?id=Tokyo&appid=7f08eea83d936e300c3ba1dc9c7ffd7a