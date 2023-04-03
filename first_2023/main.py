from geopy.geocoders import Nominatim

# calling the nominatim tool
loc = Nominatim(user_agent="Vlad")

# entering the location name
getLog = loc.geocode('Unecha')

# printing address/location name
print(getLog.address)
# Унеча, Унечское городское поселение, Унечский район,
# Брянская область, Центральный федеральный округ, Россия

print("Широта = ", getLog.latitude, '\n')
# Широта =  52.8451
print("Долгота = ", getLog.longitude)
# Долгота =  32.6867
