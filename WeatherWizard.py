
import tkinter as tk

from tkinter import Label, StringVar, ttk, font
from tkinter.constants import X

import requests

root = tk.Tk()


def get_weather(city):
    try:

        api_key = "YOUR API KEY GOES HERE"
        api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(api_url)
        weather = response.json()
        format_response(weather)

    except Exception:
        label["text"] = ("Choose a city first!")


def format_response(weather):
    name = weather["name"]
    descr = weather["weather"][0]["description"]
    temp = weather["main"]["temp"]
    f = f"""
    {name}
    Sky: {descr}
    Temperature: {temp} °C
    """
    label["text"] = f


alto = 500
ancho = 600

canvas = tk.Canvas(root, height=alto, width=ancho, bg="gray")
canvas.pack()

background_image = tk.PhotoImage(file="./Art.png")
background_label = tk.Label(canvas, image=background_image)
background_label.place(relwidth=1, relheight=1)


frameselect = tk.Frame(canvas, bg="red")
frameselect.place(relheight=0.1, relwidth=0.5, rely=0.2, relx=0.1)

choices = ["Córdoba, AR", "Buenos Aires, AR", "La Plata, AR",
           "San Fernando del Valle de Catamarca, AR", "Resistencia, AR", "Rawson, AR",
           "Corrientes, AR", "Paraná, AR", "Formosa, AR", "Mendoza, AR"]

combo = ttk.Combobox(frameselect, values=choices,)
combo.place(relx=0, rely=0, relheight=1, relwidth=0.7)


button = tk.Button(frameselect, text="Confirm", font=("Papyrus"),
                   command=lambda: get_weather(combo.get()))
button.place(anchor="se", relx=1, rely=1, relwidth=0.3, relheight=1)


frameoutput = tk.Frame(canvas, bg="yellow")
frameoutput.place(relheight=0.5, relwidth=0.5, rely=0.4, relx=0.1)

label = tk.Label(frameoutput, bg="white", font=("Papyrus", 14))
label.place(relwidth=1, relheight=1, rely=0, relx=0)


root.mainloop()
