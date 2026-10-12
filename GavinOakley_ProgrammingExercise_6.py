import re

#Define the strings that will be matched in the regular expression for the user's phone/social/zip.

#The phone number must be in 10 digit format, hyphens and parentheses optional.
phonePattern = r"^\(?\d{3}\)?-?\d{3}-?\d{4}$"

#The social security number must be in 9 digit format, and must have hyphens.
socialPattern = r"^\d{3}-\d{2}-\d{4}$"

#The zip code is in a regular 5 digit format.
zipPattern = r"^\d{5}$"

#Define the function to verify user input by matching to the above patterns.
def verify_info(phone, social, zipcode):
    verifyPhone = re.fullmatch(phonePattern, phone)
    verifySocial = re.fullmatch(socialPattern, social)
    verifyZip = re.fullmatch(zipPattern, zipcode)
#Return the value for each match so the input can be validated later.
    return verifyPhone, verifySocial, verifyZip

phone = input("Enter your phone number: ")
social = input("Enter your social security number: ")
zipcode = input("Enter your zip code: ")

#Create objects for phone, social, and zip matches so they can be used outside verify_info.
phone_match, social_match, zip_match = verify_info(phone, social, zipcode)

#Print whether or not the user's info is valid based on the value from the match.
print("Phone number:", "valid" if phone_match is not None else "Invalid phone number!")
print("Social Security number:", "valid" if social_match is not None else "Invalid social security number!")
print("Zip code:", "valid" if zip_match is not None else "Invalid zip code!")