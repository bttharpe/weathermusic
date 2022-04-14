import requests

def sun_times(lat, lon):

    SUNSET_URL = "https://api.sunrise-sunset.org/json"

    params = {
        "lat": lat,
        "lng": lon,
        "formatted": "1",
    }

    sunset_results = requests.get(SUNSET_URL, params)
    sunset_response = sunset_results.json()
    results = sunset_response["results"]

    sunset_times = {
        "sunrise": results["sunrise"],
        "sunset": results["sunset"],
        "daylength": results["day_length"]
    }
    

    return sunset_times