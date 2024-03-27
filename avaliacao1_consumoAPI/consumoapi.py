import requests

def get_weather(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&APPID={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(data):
    if 'name' not in data:
        print("Cidade não encontrada. Por favor, verifique o nome da cidade.")
    else:
        print(f"Condições climáticas para {data['name']}:")
        temperature_celsius = round(data['main']['temp'] - 273.15, 2)
        print(f"Temperatura: {temperature_celsius}°C")
        print(f"Descrição: {data['weather'][0]['description'].capitalize()}")
        print(f"Umidade: {data['main']['humidity']}%")
        print(f"Pressão atmosférica: {data['main']['pressure']} hPa")
        wind_speed_kmh = round(data['wind']['speed'] * 3.6, 2)
        print(f"Velocidade do vento: {wind_speed_kmh} km/h")

def main():
    city_name = input("Digite o nome da cidade: ")
    api_key = "9a28e765864e6ffe95cb1400515fe85a"
    weather_data = get_weather(city_name, api_key)
    display_weather(weather_data)

if __name__ == "__main__":
    main()