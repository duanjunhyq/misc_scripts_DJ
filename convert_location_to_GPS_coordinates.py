from geopy.geocoders import Nominatim
geolocator = Nominatim()
location = geolocator.geocode("Vancouver")
print(location.address)
print((location.latitude, location.longitude))
print(location.raw)
