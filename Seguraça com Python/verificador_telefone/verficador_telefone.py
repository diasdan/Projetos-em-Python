import phonenumbers

from phonenumbers import geocoder

phone_number = input('Enter phone number [format: +551100000000]: ')

phone_numbers = phonenumbers.parse(phone_number)

print(geocoder.description_for_number(phone_numbers, 'pt'))




