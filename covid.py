import requests
from win10toast import ToastNotifier
import json
import time

def info():
    r = requests.get("https://coronavirus-19-api.herokuapp.com/all")
    data = r.json()
    text = f'Confirmed cases: {data["cases"]} \nDeaths : {data["deaths"]} \nRecovered : {data["recovered"]}'

    while True:
        toast = ToastNotifier()
        toast.show_toast("COVID INFO",text,duration=20)
        time.sleep()

info()