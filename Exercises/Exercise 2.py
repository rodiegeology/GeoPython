station_names = ['Harmaja', 'Kaisaniemi', 'Kaivopuisto', 'Kumpula', 'lighthouse', 'Malmi airfield', 'Suomenlinna aaltopoiju', 'Vuosaari harbour']
station_start_years = [1989, 1844, 1904, 2005, 2003, 1937, 2016, 2012]

selected_station = "Harmaja"
print(selected_station)

station_index = station_names.index(selected_station)
station_years = 2020 - station_start_years[station_index]

print ("The Helsinki {} station has been operational for {} years.".format(selected_station,station_years))

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "November", "December")
month_avr_temp = (-3.5, -4.5, -1.0, 4.0, 10.0, 15.0, 18.0, 16.0, 11.5, 6.0, 2.0, -1.5)
selected_month = input("Which month would you like to input?")
month_index = months.index(selected_month)
print ("The average temperature in Helsinki in {} is {} degrees Celsius".format(selected_month, month_avr_temp[month_index]))
