import re, pyperclip

# create regex for phone numbers
phoneRegex = re.compile(r'''(((\d\d\d) | (\(\d\d\d\)))?(\s|-)\d\d\d-\d\d\d\d(((ext(\.)?\s)|x) (\d{2,5}))?)''', re.VERBOSE)

# create a regex for email addresses
emailRegex = re.compile(r'''[a-zA-Z0-9_.+]+@[a-zA-Z0-9_.+]+''', re.VERBOSE)

#get the text off the clipboard
text = pyperclip.paste()

#extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

#copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)