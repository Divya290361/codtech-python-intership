import requests
import matplotlib.pyplot as plt

API_KEY = '4845cd6265a7ad258d4c4bd8f1b32ba3'  # ✅ your API key
CITY = 'Mumbai'

# Build the API URL
url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

# Make the API call
response = requests.get(url)
print("API call made...")
print("Response:", response.status_code)

data = response.json()

if data.get("main"):
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']

    print(f"\nWeather in {CITY}:")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Pressure: {pressure} hPa")

    # Bar Graph
    labels = ['Temperature (°C)', 'Humidity (%)', 'Pressure (hPa)']
    values = [temp, humidity, pressure]
    colors = ['skyblue', 'lightgreen', 'salmon']

    plt.bar(labels, values, color=colors)
    plt.title(f'Current Weather in {CITY}')
    plt.ylabel('Values')
    plt.grid(True)
    plt.show()
else:
    print("Something went wrong: Check your API key or city.")