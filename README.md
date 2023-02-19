# Masjid Mate

![yasmine-arfaoui-R6rh5ttDO-4-unsplash](https://user-images.githubusercontent.com/86541956/219946563-0c419f04-0b8b-43e9-8165-bc5e63a162a2.jpg)


Masjid Mate is a Python app that helps Muslims find nearby mosques and catch prayers on time. It consists of three scripts:

- `location.py`: finds the user's location using the Google Maps API.
- `mosques.py`: finds the nearest mosques using the Google Maps API.
- `prayer.py`: finds the upcoming prayer times using the Aladhan API. This script uses Moonsighting Comittee (method 15) method for calculations by default but can be changed, refer to: https://aladhan.com/prayer-times-api#GetMethods for more information.

Masjid Mate is a work in progress, and the `catch_prayer.py` script, which combines these three scripts to provide users with upcoming prayer times at nearby mosques, is still under development.

## Usage

To use Masjid Mate, follow these steps:

1. Set up your Google Maps and Aladhan API keys by creating a `api_keys.py` file in the root directory of the project and defining the following variables:

   ```python
   GOOGLE_MAPS_API_KEY = "your_google_maps_api_key"
   ALADHAN_API_KEY = "your_aladhan_api_key"
   ```

2. Run the `location.py` script to find your current location:

   ```bash
   python location.py
   ```

3. Run the `mosques.py` script to find the nearest mosques:

   ```bash
   python mosques.py
   ```

4. Run the `prayer.py` script to find the upcoming prayer times:

   ```bash
   python prayer.py
   ```

Note that the `catch_prayer.py` script is still under development and is not yet available for use.

## Requirements

Masjid Mate requires the following Python libraries:

- googlemaps
- requests
- datetime

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Author

Masjid Mate was created by Algi.

## Resources

I used the Google Maps API to retrieve the user's location and find nearby mosques. Additionally, I used the Aladhan API to retrieve the prayer times for the user's location. To interact with these APIs, I used the googlemaps and requests Python libraries. Image credits: Yasmine Arfaoui, Unsplash
