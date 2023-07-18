from validator_collection import validators, errors

try:
    if validators.email(input("What's your email address? ")):
        print("Valid")
except (errors.EmptyValueError, errors.InvalidEmailError):
    print("Invalid")
