import phonenumbers
from phonenumbers import geocoder
ph1=phonenumbers.parse("+919874852004")

print("Location:-\n")
print(geocoder.description_for_number(ph1,"en"))
