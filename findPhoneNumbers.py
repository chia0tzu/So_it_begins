# def to check if it is valid US phone number

def isPhoneNumber(text):    # 123-123-
    if len(text) != 12:
        return False    #not phone numbered size
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False    #no area code
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False    #missing 2nd dash
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False    #missing last 4 digits
    return True

print(isPhoneNumber('123-123-1234'))

# scan a text to find valid(US) phone numbers
message = "Call me now at 123-123-1234 or later on 321-321-4321"
foundNumber = False
for i in range(len(message)):
    part = message[i:i+12]
    if isPhoneNumber(part):
        print("Phone number found: " + part)
        foundNumber = True
if not foundNumber:
    print("We could not found phone number")