import requests, geocoder
import tkinter as tk

API_KEY = "440605aa98d755533e35848fd00e8ec9"
g=geocoder.ip("me")   
city = g.city
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

root=tk.Tk()
root.title("WEATHERAPP")

if "main" in data:
    text = f"City: {city}\nTemperature: {data['main']['temp']} °C\nHumidity: {data['main']['humidity']} %\nCondition: {data['weather'][0]['description']}"
else:
   text = f"Error: {data.get('message', 'Unknown error')}"


label=tk.Label(root,text=text,font=("Arial",14))
label.pack(padx=20,pady=20)

root.mainloop()
