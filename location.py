from api_keys import GOOGLE_MAPS_API_KEY
import requests

API_KEY = GOOGLE_MAPS_API_KEY


def get_location():
    try:
        # send a request to the Google Maps API to get the user's current location
        url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={API_KEY}"
        response = requests.post(url)
        data = response.json()

        # extract the latitude and longitude from the response
        location = data.get("location", {})
        lat = location.get("lat")
        lng = location.get("lng")

        # return the latitude and longitude as a tuple
        return lat, lng

    except requests.exceptions.RequestException as e:
        print("Error: ", e)


if __name__ == '__main__':
    location = get_location()
    print(location)
