from api_keys import GOOGLE_MAPS_API_KEY
import requests
from location import get_location


def find_nearest_mosques():
    try:
        location = get_location()
        # send a request to the Google Places API to find the nearest mosques or masjids
        url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location[0]},{location[1]}&radius=5000&type=mosque&key={GOOGLE_MAPS_API_KEY}"
        response = requests.get(url)
        data = response.json()

        # loop through the results and send a request to the Google Distance Matrix API to get the walking distance to each mosque
        for result in data["results"]:
            place_id = result["place_id"]
            name = result["name"]
            address = result["vicinity"]

            # send a request to the Google Distance Matrix API to get the walking distance to this mosque
            distance_url = f"https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins={location[0]},{location[1]}&destinations=place_id:{place_id}&key={GOOGLE_MAPS_API_KEY}"
            distance_response = requests.get(distance_url)
            distance_data = distance_response.json()
            distance = distance_data["rows"][0]["elements"][0]["distance"]["text"]

            # print out the name, address, and walking distance for this mosque
            print(f"Name: {name}")
            print(f"Address: {address}")
            print(f"Walking distance: {distance}")

    except requests.exceptions.RequestException as e:
        print("Error: ", e)


if __name__ == '__main__':
    find_nearest_mosques()
