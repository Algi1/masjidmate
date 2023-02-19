import requests
from api_keys import ALADHAN_API_KEY
from location import get_location
import datetime


def find_upcoming_prayer(location):
    try:
        # send a request to the Aladhan API to get the prayer times for the user's location
        url = f"https://api.aladhan.com/v1/calendar?latitude={location[0]}&longitude={location[1]}&method=15&month={datetime.date.today().month}&year={datetime.date.today().year}&adjustment=1&school=1"
        response = requests.get(url, headers={"X-API-KEY": ALADHAN_API_KEY})
        data = response.json()

        # extract the prayer times for today from the response
        timings = data["data"][0]["timings"]

        # find the upcoming prayer
        for prayer, time in timings.items():
            time_without_tz = time.split()[0]
            prayer_time = datetime.datetime.combine(datetime.date.today(
            ), datetime.datetime.strptime(time_without_tz, '%I:%M').time())
            if prayer_time > datetime.datetime.now():
                time_until_prayer = prayer_time - datetime.datetime.now()
                hours, remainder = divmod(
                    time_until_prayer.total_seconds(), 3600)
                minutes, seconds = divmod(remainder, 60)
                time_until_prayer = f"{int(hours)} hours, {int(minutes)} minutes"
                return f"Next prayer is {prayer} in {time_until_prayer} at {time}"

    except requests.exceptions.RequestException as e:
        return "Error: " + str(e)


if __name__ == '__main__':
    location = get_location()
    upcoming_prayer = find_upcoming_prayer(location)
    print(upcoming_prayer)
