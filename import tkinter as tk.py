import tkinter as tk
from tkinter import ttk
import requests
from PIL import Image, ImageTk

def get_weather():
    city = city_entry.get()
    api_key = "42b96386abd425f07690af3d833519c3"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        weather_data = response.json()
        display_weather(weather_data)
    else:
        weather_label.config(text="Error fetching weather data")

def display_weather(data):
    description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]

    # Get weather icon
    icon_code = data["weather"][0]["icon"]
    icon_url = f"http://openweathermap.org/img/w/{icon_code}.png"
    icon_data = requests.get(icon_url, stream=True).content
    icon = ImageTk.PhotoImage(Image.open(BytesIO(icon_data)))

    # Update GUI elements
    weather_label.config(text=f"Weather: {description}")
    temp_label.config(text=f"Temperature: {temperature}°C")
    humidity_label.config(text=f"Humidity: {humidity}%")
    weather_icon.config(image=icon)
    weather_icon.image = icon  # Keep a reference to prevent garbage collection

# Create the main window
root = tk.Tk()
root.title("Weather Forecast App")

# Create GUI elements
city_label = tk.Label(root, text="Enter City:", font=("Helvetica", 14))
city_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

city_entry = tk.Entry(root, font=("Helvetica", 14))
city_entry.grid(row=0, column=1, padx=10, pady=10)

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather, font=("Helvetica", 14))
get_weather_button.grid(row=0, column=2, padx=10, pady=10)

weather_label = tk.Label(root, text="", font=("Helvetica", 16))
weather_label.grid(row=1, column=0, columnspan=3, pady=10)

temp_label = tk.Label(root, text="", font=("Helvetica", 14))
temp_label.grid(row=2, column=0, columnspan=3)

humidity_label = tk.Label(root, text="", font=("Helvetica", 14))
humidity_label.grid(row=3, column=0, columnspan=3)

weather_icon = tk.Label(root)
weather_icon.grid(row=4, column=0, columnspan=3, pady=10)

# Run the main loop
root.mainloop()
