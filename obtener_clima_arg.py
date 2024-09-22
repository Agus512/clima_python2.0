import requests
import time

OWM_API_KEY = ""


def obtener_clima(lugar: str):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={lugar},AR&appid={OWM_API_KEY}&units=metric&lang=es"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperatura = data['main']['temp']
        descripcion = data['weather'][0]['description']
        print(f"El clima en {lugar} es {descripcion} con una temperatura de {temperatura}°C.")
    else:
        print(f"No se pudo obtener el clima para {lugar}.")

lugar = input("Ingresar lugar de ARGENTINA donde deseas obtener el clima:")
obtener_clima(lugar)
