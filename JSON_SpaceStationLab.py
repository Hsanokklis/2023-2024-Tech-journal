"""
Description: Write a program of your choice that manipulates JSON, either by leveraging a public API or using an existing JSON dataset.

The program I wrote pull from an API that returns information about the International Space Station(ISS). My code
specifically returns the location of the ISS.


Author: Hannelore Sanokklis
Class: CSI-160-01
Assignment: JSON API Lab
Due Date: 12/01/2023


Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)

Links Used:

Help on using the "request" library:
https://stackoverflow.com/questions/645312/what-is-the-quickest-way-to-http-get-in-python

"Where the ISS at?" REST API Documentation
https://wheretheiss.at/w/developer#:~:text=Welcome%20to%20the%20WTIA%20REST,TLE%20data%20on%20the%20ISS.

Help w/ syntax for google map links:
https://stackoverflow.com/questions/1801732/how-do-i-link-to-google-maps-with-a-particular-longitude-and-latitude/52943975#52943975
"""

import requests
from geopy.geocoders import Nominatim

# Make request to ISS API
r = requests.get("https://api.wheretheiss.at/v1/satellites/25544")

# Check the HTTP status of the website to make sure the request is completed successfully
if r.status_code != 200:
    print("API request issue")
    exit()

# Dictionary of ISS attributes
data = r.json()

# Get coordinates from the ISS API response
coordinates = (data['latitude'], data['longitude'])
print("Coordinates of the ISS:", coordinates)

# Initialize Nominatim API
geolocator = Nominatim(user_agent="MyApp")

# Use geocoding to get the address information
location = geolocator.reverse(coordinates)

if location is not None:
    # Extract city, state, and country from geopy address
    address = location.raw['address']
    city = address.get('city', '')
    state = address.get('state', '')
    country = address.get('country', '')

    print("City, State, Country of the ISS location:", city, state, country)
    # returns a google map with the coordinates
    print("https://www.google.com/maps/search/?api=1&query="+str(data['latitude'])+","+str(data['longitude']))

else:
    # If there is no exact location data, you can still see the location via it's coordinates on Google maps
    print("No address information available for the given coordinates. (It's probably over the ocean)")
    # returns a google map with the coordinates
    print("Check out it's location here --->", "https://www.google.com/maps/search/?api=1&query="+str(data['latitude'])+","+str(data['longitude']))

