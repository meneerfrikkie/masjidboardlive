import requests
from bs4 import BeautifulSoup

# URL of the Masjid Board page
url = "https://masjidboardlive.com/boards/?southdale-ebrahim"

# Send a GET request to the page
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Prayer names and their corresponding IDs
    prayers = {
        'Fajr': 'fajr',
        'Zuhr': 'zuhr',
        'Asr': 'asr',
        'Maghrib': 'maghrib',
        'Isha': 'esha'
    }

    # Dictionary to store the extracted Salaah times
    salaah_times = {}

    # Loop through each prayer and extract the Athan and Jamaah times
    for prayer, prayer_id in prayers.items():
        athan_time = soup.find('h5', id=f'{prayer_id}Athan').text.strip()
        jamaah_time = soup.find('h5', id=f'{prayer_id}Jamaah').text.strip()
        salaah_times[prayer] = {'Adhan': athan_time, 'Jamaah': jamaah_time}

    # Print the Salaah times
    print("Salaah Times:")
    for salaah, times in salaah_times.items():
        print(f"{salaah}: Adhan - {times['Adhan']}, Jamaah - {times['Jamaah']}")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
