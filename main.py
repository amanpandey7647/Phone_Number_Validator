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
            print("Location: {}, Carrier: {}, Timezone: {}".format(location, carrier_name, time_zone[0]))
        else:
            print("Provided number is not a valid number")
    else:
        print("Provided number is not a possible number")
except Exception as e:
    print(e)
