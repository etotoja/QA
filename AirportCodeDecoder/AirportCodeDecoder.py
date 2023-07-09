from FlightRadar24.api import FlightRadar24API
import requests
import json
from datetime import datetime, timedelta

fr_api = FlightRadar24API()

# code below is for educational purpose only, doesnt affect app
{'name': 'Krakow John Paul II International Airport', 'code': {'iata': 'KRK', 'icao': 'EPKK'}, 'position': {'latitude': 50.077728, 'longitude': 19.78483, 'altitude': 791, 'country': {'id': 176, 'name': 'Poland', 'code': 'PL', 'codeLong': 'POL'}, 'region': {'city': 'Krakow'}}, 'timezone': {'name': 'Europe/Warsaw', 'offset': 7200, 'offsetHours': '2:00', 'abbr': 'CEST', 'abbrName': 'Central European Summer Time', 'isDst': True}, 'visible': True, 'website': 'http://www.krakowairport.pl/en', 'stats': {'arrivals': {'delayIndex': 0.33, 'delayAvg': None, 'total': 854, 'hourly': {'17': 30, '16': 51, '15': 44, '14': 53, '13': 57, '12': 61, '11': 81, '10': 71, '9': 57, '8': 73, '7': 48, '6': 0, '5': 0, '4': 0, '3': 0, '2': 0, '1': 0, '0': 0, '23': 68, '22': 80, '21': 45, '20': 35, '19': 0, '18': 0}, 'stats': [30, 51, 44, 53, 57, 61, 81, 71, 57, 73, 48, 0, 0, 0, 0, 0, 0, 0, 68, 80, 45, 35, 0, 0]}, 'departures': {'delayIndex': 1.42, 'delayAvg': None, 'total': 898, 'hourly': 
{'17': 57, '16': 66, '15': 43, '14': 52, '13': 62, '12': 73, '11': 64, '10': 66, '9': 73, '8': 69, '7': 59, '6': 56, '5': 61, '4': 27, '3': 0, '2': 0, '1': 0, '0': 0, '23': 0, '22': 0, '21': 19, '20': 31, '19': 10, '18': 10}, 'stats': [57, 66, 
43, 52, 62, 73, 64, 66, 73, 69, 59, 56, 61, 27, 0, 0, 0, 0, 0, 0, 19, 31, 10, 10]}}}
# code above is for educational purpose only, doesnt affect app

while True:
    try:
        input_apt = input("Enter 3-letter IATA code or 4-letter ICAO code for chosen airport: ")

        selected_apt = input_apt
        selected_apt_data = fr_api.get_airport(selected_apt)


        apt_name = selected_apt_data['name']
        apt_iata = selected_apt_data['code']['iata']
        apt_icao = selected_apt_data['code']['icao']
        apt_country = selected_apt_data['position']['country']['name']
        apt_city = selected_apt_data['position']['region']['city']

        apt_time = selected_apt_data['timezone']['offsetHours'] 
        def calculate_timezone(move):
            # Getting current date and time in UTC
            currenttime = datetime.utcnow() 

            # Calculating time split in other using "hours:minutes"
            hours, minutes = map(int, move.split(':'))

            # Creating timedelta using timesplitting
            delta = timedelta(hours=hours, minutes=minutes)

            # Calculating new time based on local's user time and offset hours
            new_time_and_date = currenttime + delta

            # Returning new time and date in "HH:MM" format, erasing the date, seconds and miliseconds
            return str(new_time_and_date)[11:16]

        # Function call for selected offset
        apt_localtime = calculate_timezone(apt_time)


        apt_timezone = selected_apt_data['timezone']['abbrName']

        print(f"{apt_name}, also known byt its IATA code {apt_iata} or ICAO code {apt_icao}, lays in {apt_city}, {apt_country}. Local time is {apt_localtime} ")
        
        break
    except TypeError:
        print(f"Selected code: '{selected_apt}' does not exist as IATA or ICAO code!")
        print("Rerunning program...")
        print(" ")
        