try:
    import phonenumbers
except:
    import os
    os.system("pip3 install phonenumbers")
    import phonenumbers

import phonenumbers
from phonenumbers import geocoder, carrier, timezone

number = input("Enter the phone number to validate along with sign and country code: ")
try:
    parsed_number = phonenumbers.parse(number)
    is_possible = phonenumbers.is_possible_number(parsed_number)
    is_valid = phonenumbers.is_valid_number(parsed_number)
    if is_possible:
        if is_valid:
            print(parsed_number)
            location = geocoder.description_for_number(parsed_number, "en")
            carrier_name = carrier.name_for_number(parsed_number, "en")
            time_zone = timezone.time_zones_for_number(parsed_number)
            valid = phonenumbers.is_valid_number(parsed_number) 
            possible = phonenumbers.is_possible_number(parsed_number) 
            Region = geocoder.description_for_number(parsed_number, 'en') 
            print("Location: {}, Carrier: {}, Timezone: {}, valid: {}, possible: {}, Region: {}".format(location, carrier_name, time_zone[0], valid, possible, Region))
        else:
            print("Provided number is not a valid number")
    else:
        print("Provided number is not a possible number")
except Exception as e:
    print(e)
