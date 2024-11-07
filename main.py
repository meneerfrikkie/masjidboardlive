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
    
    # Dictionary to store the extracted Salaah times
    salaah_times = {}

    # Extracting Fajr time
    fajr_athan = soup.find('h5', id='fajrAthan').text.strip()
    fajr_jamaah = soup.find('h5', id='fajrJamaah').text.strip()
    salaah_times['Fajr'] = {'Adhan': fajr_athan, 'Jamaah': fajr_jamaah}

    # Extracting Zuhr time
    zuhr_athan = soup.find('h5', id='zuhrAthan').text.strip()
    zuhr_jamaah = soup.find('h5', id='zuhrJamaah').text.strip()
    salaah_times['Zuhr'] = {'Adhan': zuhr_athan, 'Jamaah': zuhr_jamaah}

    # Extracting Asr time
    asr_athan = soup.find('h5', id='asrAthan').text.strip()
    asr_jamaah = soup.find('h5', id='asrJamaah').text.strip()
    salaah_times['Asr'] = {'Adhan': asr_athan, 'Jamaah': asr_jamaah}

    # Extracting Maghrib time
    maghrib_athan = soup.find('h5', id='maghribAthan').text.strip()
    maghrib_jamaah = soup.find('h5', id='maghribJamaah').text.strip()
    salaah_times['Maghrib'] = {'Adhan': maghrib_athan, 'Jamaah': maghrib_jamaah}

    # Extracting Isha time
    isha_athan = soup.find('h5', id='eshaAthan').text.strip()
    isha_jamaah = soup.find('h5', id='eshaJamaah').text.strip()
    salaah_times['Isha'] = {'Adhan': isha_athan, 'Jamaah': isha_jamaah}

    # Print the Salaah times
    print("Salaah Times:")
    for salaah, times in salaah_times.items():
        print(f"{salaah}: Adhan - {times['Adhan']}, Jamaah - {times['Jamaah']}")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
