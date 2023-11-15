import requests
import pandas as pd
from bs4 import BeautifulSoup

# Send a GET request to the URL
url = "https://www.qantas.com/hotels/properties/18482?adults=2&checkIn=2023-10-30&checkOut=2023-10-31&children=0&infants=0&location=London%2C%20England%2C%20United%20Kingdom&page=1&payWith=cash&searchType=list&sortBy=popularity"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the room details on the page
room_details = soup.find_all("div", class_="room-details")

# Create a list to store the room details
room_list = []

# Extract the relevant information from each room detail
for room in room_details:
    room_name = room.find("h3").text.strip()
    room_price = room.find("span", class_="price").text.strip()
    room_description = room.find("p", class_="description").text.strip()
    
    # Append the room details to the list
    room_list.append([room_name, room_price, room_description])

# Create a DataFrame from the room list
df = pd.DataFrame(room_list, columns=["Room Name", "Price", "Description"])

# Save the DataFrame to an Excel file
df.to_excel("room_details.xlsx", index=False)
