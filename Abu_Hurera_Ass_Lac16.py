import requests

# GET Request Practice
# names = ['Ali','Hamza','Sara','Ahmad']

# for name in names:
#    response = requests.get(f"https://api.agify.io?name={name}")
#    if response.status_code == 200:
#       data = response.json()
#       print(f"Age for name {name}: {data["age"]}")
#    else:
#       print("Faild request due to error")

# POST Request Practice
# url = "https://httpbin.org/post"
# course = {
#    "course":"Python",
#    "level":"Beginner"
# }
# response = requests.post(url,data=course)
# print(response.json())

# Error Handling Practice
# try:
#    invalid_api_url = requests.get("https://invalidapi.myapi.il")
#    if invalid_api_url.status_code != 200:
#       print(f"Error: Unable to fetch data (Status Code: {invalid_api_url.status_code}")
# except requests.exceptions.RequestException as e:
#    print("Custom Error: Invalid API URL or Connection Failed.")
#    print("Details:", e)

# API Cleint Mini Project
print("=== Weather API Client ===")
print("You can check Weather of These Cities:\n(karchi,lahore,islamabad,tandobago,badin,golarchi,matli,talhar)")
city = input("Enter a city name: ").strip()

# Simple city -> coordinates map (you can add more)
city_coords = {
    "karachi": {"lat": 24.8607, "lon": 67.0011},
    "lahore": {"lat": 31.5497, "lon": 74.3436},
    "islamabad": {"lat": 33.6844, "lon": 73.0479},
    "tandobago": {"lat": 24.7887164, "lon": 68.9655333},
    "badin": {"lat": 24.6557, "lon": 68.8372},
    "matli": {"lat": 24.0444, "lon": 68.6589},
    "talhar": {"lat": 24.84150, "lon": 68.83840},
    "golarchi": {"lat": 24.6532363, "lon": 68.83840}
}

if city.lower() in city_coords:
    lat = city_coords[city.lower()]["lat"]
    lon = city_coords[city.lower()]["lon"]

    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(weather_url)

    if response.status_code == 200:
        data = response.json()
        current = data.get("current_weather", {})

        print(f"\nWeather in {city.title()}:")
        print(f"Temperature: {current.get('temperature', 'N/A')}°C")
        print(f"Windspeed: {current.get('windspeed', 'N/A')} km/h")
        print(f"Wind Direction: {current.get('winddirection', 'N/A')}°")
    else:
        print("Failed to fetch weather data.")
else:
    print("City not found in the list. Try Karachi, Lahore, Islamabad, or Tanod Bago.")
