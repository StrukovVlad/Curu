from geopy.geocoders import Nominatim
from geopy.distance import geodesic as gd

def distance_towns(x: str, y: str) -> float :
    A = (loc.geocode(x).latitude, loc.geocode(x).longitude)
    B = (loc.geocode(y).latitude, loc.geocode(y).longitude)
    return gd(A, B)


def func(town):
    getLog = loc.geocode(town)
    return(f"Широта города {town.title()} =  {getLog.latitude}\
           \nДолгота города {town.title()} =  {getLog.longitude}")


town_1 = input("Пожалуйста введите название первого города ,en :  ")
town_2 = input("Пожалуйста введите название второго города ,en :  ")
loc = Nominatim(user_agent="Vlad")
print(func(town_1), func(town_2), sep='\n')
print()
print(f"Расстояние между городами : {distance_towns(town_1, town_2 )}")

# Пожалуйста введите название первого города ,en :  minsk
# Пожалуйста введите название второго города ,en :  grodno
# Широта города Minsk =  53.9024716
# Долгота города Minsk =  27.5618225
# Широта города Grodno =  53.6834599
# Долгота города Grodno =  23.8342648

# Расстояние между городами : 246.82617716292708 km

