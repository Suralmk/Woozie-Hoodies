import phonenumbers

def validate_phone_number(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number, None)
        return phonenumbers.is_valid_number(parsed_number)
    except phonenumbers.phonenumberutil.NumberParseException:
        return False

# Example usage:
# phone_number = "+1234567890" +251914719859  # Replace with your phone number
# if validate_phone_number(phone_number):
#     print("Valid phone number")
# else:
#     print("Invalid phone number")
