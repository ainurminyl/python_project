import eel
import pyowm

owm = pyowm.OWM("5b9dd625b50e752ef382ab9a7b9f6377")

@eel.expose
def get_weather(place):
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(place)
    w = observation.weather

    temp = w.temperature('celsius')['temp']

    return "В городе " + place + " сейчас " + str(temp) + " градусов!"

eel.init("web")

eel.start("main.html", size=(700,700))
