--""""
Description: I wrote a program with an interactive menu that allows a user to select from 6 Space APIs and get data
about different space objects and planets!


Author: Hannelore Sanokklis
Class: CSI-160-01
Assignment: Final Project
Due Date: 12/11/2023


Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
Links used:

APIs used:
NASA API's: https://api.nasa.gov/
Where is the ISS: https://wheretheiss.at/
NASA picture of the day: https://api.nasa.gov/planetary/apod
NASA Earth Picture: https://api.nasa.gov/EPIC/api/natural/images?api_key=DEMO_KEY
NASA EPIC API: https://epic.gsfc.nasa.gov/about/api
NASA Asteroids NeoW: https://api.nasa.gov/neo/rest/v1/neo/browse/
NASA Mars rover pictures API: https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2015-6-3&api_key=DEMO_KEY
How many people are in space right now: https://api.open-notify.org/astros.json
"""

import requests
from geopy.geocoders import Nominatim

### User defined Functions

# Option 1 People in Space
def people_in_space():
    """
    Gets the number and names of the people in space from https://api.open-notify.org/astros.json
    :return: The number of people in space and their names
    """
    # Make request to the API
    r = requests.get("http://api.open-notify.org/astros.json")

    # Check the HTTP status of the website to make sure the request is completed successfully
    if r.status_code != 200:
        print("API request issue")
        exit()

    # Dictionary of people in space attributes
    data = r.json()

    # Dictionary of the people in space
    people_data = data['people']
    print("\nThere are", data['number'], "astronauts in space! And you're not one of them!")

    print("\nTheir names are: \n")
    n = 1
    # adds a number in front of their name
    for person in people_data:
        print("\t" + str(n) + ". " + person['name'])
        n += 1
    input("\nPress Enter to return to the menu...")

# Option 2 Where is the ISS right now

def Where_Is_ISS():
    """
    Get the coordinates of the ISS using https://wheretheiss.at/, and converts them to a location using the Geopy library
    :return: The coordinates of the ISS and a link to Google maps to show its location
    """
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

    m = requests.get("https://api.wheretheiss.at/v1/coordinates/" + str(data['latitude']) + "," + str(data['longitude']))

    # Check the HTTP status of the website to make sure the request is completed successfully
    if m.status_code != 200:
        print("API request issue")
        exit()

    # Another Dictionary of ISS attributes that include additional attributes
    data2 = m.json()

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

    # Pull from the data2 json set to get the timezone of the ISS
    print("The ISS is in this timezone: ", data2['timezone_id'])

    # User must hit enter to go back to the menu
    input("\nPress Enter to return to the menu...")


# Option 3 Astronomy Picture of the Day

def split_sting(big_string):
    """
    Passing through the picture_of_the_day function to break up a paragraph of text
    :param big_string:
    :return: will be passed through the picture_of_the_day function to split up the explanation of the picture
    """
    paragraph = big_string
    description_sentences = paragraph.split(".")
    return description_sentences
def picture_of_the_day():
    """
    Using the NASA space picture of the day API (https://api.nasa.gov/planetary/apod?api_key=inUsIJJJE5hJYaIMrLK4so0MrXqewAGpcA2x0P2W)
    this function queries the API to output the daily space picture!
    :return: The picture URL, title, and description of the daily space picture
    """

    # Make request to the API
    r = requests.get("https://api.nasa.gov/planetary/apod?api_key=inUsIJJJE5hJYaIMrLK4so0MrXqewAGpcA2x0P2W")

    # Check the HTTP status of the website to make sure the request is completed successfully
    if r.status_code != 200:
        print("API request issue")
        exit()

    # Splits the string of text that is the explanation so its easier to read in the output
    data = r.json()
    print("\nTitle: " + str(data['title']))
    print("\nAstronomy Picture of the Day!: " + str(data['hdurl']))
    explanation_sentences = split_sting(data['explanation'])
    print("\nImage Description:\n ")
    for sentence in explanation_sentences:
        #gets rid of extra space characters with .strip
        print("\t", sentence.strip())
    input("\nPress Enter to return to the menu...")

# Option 4 Asteroids Close to Earth
def asteriods_close_to_earth():
    """
    Using https://api.nasa.gov/neo/rest/v1/neo/browse/ takes data about asteroids close to earth and displays information about them
    :return: A list of asteroids that have been and will be close to earth based on their orbits
    """
    # Make request to the API
    r = requests.get("https://api.nasa.gov/neo/rest/v1/neo/browse?api_key=inUsIJJJE5hJYaIMrLK4so0MrXqewAGpcA2x0P2W")

    # Check the HTTP status of the website to make sure the request is completed successfully
    if r.status_code != 200:
        print("API request issue")
        exit()

    # Dictionary of Asteroids
    data = r.json()
    near_earth = data["near_earth_objects"]
    # Loops through the dictionaries within the lists
    for object in near_earth:
        number_of_approaches = len(object["close_approach_data"])
        index_in_present = int(number_of_approaches / 2)
        print("\nAsteroid Name:", object['name_limited'])
        print("Velocity in MPH: " , object['close_approach_data'][-1]['relative_velocity']['miles_per_hour'])
        print("Potentially Hazardous?: ", object['is_potentially_hazardous_asteroid'])
        print("This is when it was last near earth: ", object["close_approach_data"][0]["close_approach_date_full"])
        print("This is when it will be near earth in the future: ", object["close_approach_data"][-1]["close_approach_date_full"])
        print("This is when the asteroid might be close to earth again: ", object["close_approach_data"][index_in_present]["close_approach_date_full"],"\n")
    input("\nPress Enter to return to the menu...")

# Option 5 Mars Rover Pictures
def Mars_Rover_Pictures(user_date):
    """
    Using https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2015-6-3&api_key=DEMO_KEY to get pictures from the Mars Rover
    :param user_date: Input from user of a data they want to see pictures from
    :return: List of Mars rover information along with pictures from the date specified by the user
    """
    # Make request to the API
    r = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=" + user_date + "&api_key=inUsIJJJE5hJYaIMrLK4so0MrXqewAGpcA2x0P2W")

    # Check the HTTP status of the website to make sure the request is completed successfully
    if r.status_code != 200:
        print("API request issue")
        exit()

    # Dictionary of Mars rover information
    data = r.json()
    if "photos" not in data.keys():
        print("There is no photo information")
        exit()
    if data["photos"] != []:
        print("\nRover Information: \n")
        print("\tRover Name: " + data['photos'][0]['rover']['name'])
        print("\tRover Launch Date: " + data['photos'][0]['rover']['launch_date'])
        print("\tRover Landing Date: " + data['photos'][0]['rover']['landing_date'])
        print("\nPicture Information: \n")
        print("Date: " + data['photos'][0]['earth_date'] + "\n")
        print("Front Hazard Avoidance Camera 1:" + data['photos'][0]['img_src'])
        print("Front Hazard Avoidance Camera 2:" + data['photos'][1]['img_src'])
        print("Rear Hazard Avoidance Camera 1 :" + data['photos'][2]['img_src'])
        print("Rear Hazard Avoidance Camera 2:" + data['photos'][3]['img_src'])
        print("Navigation Camera 1:" + data['photos'][4]['img_src'])
        print("Navigation Camera 2:" + data['photos'][5]['img_src'])
    else:
        print("No photos exist at this date. Try another date")
    input("\nPress Enter to return to the menu...")

# Option 6 Earth Picture of the Day
def picture_of_earth():
    """
    Using https://api.nasa.gov/EPIC/api/natural/images?api_key=DEMO_KEY this function spits out a link to a picture of earth
    :return: A picture taken of earth from the day before
    """
    # Make request to the API
    r = requests.get("https://api.nasa.gov/EPIC/api/natural/images?api_key=inUsIJJJE5hJYaIMrLK4so0MrXqewAGpcA2x0P2W")

    # Check the HTTP status of the website to make sure the request is completed successfully
    if r.status_code != 200:
        print("API request issue")
        exit()

    # Dictionary Earth information
    data = r.json()

    image_name = data[0]["image"]
    image_caption = data[0]["caption"]
    date_stamp = data[0]["date"]

    # (example for end of URL) 2015/10/31/png/epic_1b_20151031074844.png
    # Spliting the URL to get the image in a link
    image_url = "https://epic.gsfc.nasa.gov/archive/natural/"
    date = date_stamp.split(" ")[0]
    year,month,day = date.split("-")

    print('\nCheck out this cool image of earth!\n')
    print("This is the date the picture was take: " + str(date_stamp))
    print(image_caption)
    print("Here's the Image URL!: " + image_url + year + "/" + month + "/" + day + "/png/" + image_name + ".png")
    # Link Referenced https://www.w3schools.com/python/ref_string_split.asp
    input("\nPress Enter to return to the menu...")


# The starting menu to choose options
def display_menu():
    """
    A menu with 7 options
    :return: The menu options that are defined in the main() function
    """
    print("\nWelcome to Hanne's Awesome Space API project! Choose an option below!")
    print("\nOptions:")
    print("\t1. How many people are in space right now?")
    print("\t2. Where is the International Space Station(ISS) right now?")
    print("\t3. Astronomy Picture of the Day")
    print("\t4. Asteroids Close to Earth")
    print("\t5. Mars Rover Pictures")
    print("\t6. Earth Picture of the Day")
    print("\t7. Exit")

def get_user_choice():
    try:
        choice = int(input("Enter your choice (1-7): "))
        return choice
    except ValueError:
        print("Invalid input. Please enter a number.")
        return -1


def main():
    """
    Prints a functional menu for the user to pick options that are defined by functions
    :return: function called by user choice
    """
    while True:
        display_menu()
        choice = get_user_choice()


        if choice == 1:
            people_in_space()
        elif choice == 2:
            Where_Is_ISS()
        elif choice == 3:
            picture_of_the_day()
        elif choice == 4:
            asteriods_close_to_earth()
        elif choice == 5:
            Mars_Rover_Pictures(input("Please input a date in the format \"YYYY-MM-DD\": " ))
        elif choice == 6:
            print(picture_of_earth())
        elif choice == 7:
            print("Exiting the program. Live Long and Prosper!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()

