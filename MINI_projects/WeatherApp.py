import requests


def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        print(f"Weather in {city}: {weather}, Temperature: {temp}°C")
    else:
        print("City not found or API error.")


DEFAULT_API_KEY = "aef7d962efe2c721ff9343720943aa0c"

def main():
    print("Welcome to the Weather App!")
    city = input("Enter city name: ")
    api_key = DEFAULT_API_KEY
    get_weather(city, api_key)

if __name__ == "__main__":
    main()
