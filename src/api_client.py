import requests

def get_location(ip):
    url = f"https://freeipapi.com/api/json/{ip}"
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    data = response.json()
    #import ipdb; ipdb.set_trace()  # Debugging breakpoint
    return{
        "country": data["countryName"],
        "region": data["regionName"],
        "city": data["cityName"]
    }