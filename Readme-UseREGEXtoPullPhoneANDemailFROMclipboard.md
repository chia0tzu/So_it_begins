# Readme - Regex

Use regular expresions to pull data from a clipboard.
In this example, i will represent how to pull US phone numbers and emaill addresses.

```
import re, pyperclip

#Step1: create regex for phone numbers
phoneRegex = re.compile(r'''
#examples of the phone numbers in the US: 123-123-1234, 123-1234, (123) 123-1234, 123-1234 ext 12345, ext. 12345, x12345
(
((\d\d\d) | (\(\d\d\d\)))?   # area code (optional)
(\s|-)                      #firts separtor
\d\d\d                      #first 3 digits
-                           #separator
\d\d\d\d                    #last 4 digits
(((ext(\.)?\s)|x)             #extension word-part (optional)
 (\d{2,5}))?                #extension number-part (optional)
)
''', re.VERBOSE)

#Step2: create a regex for email addresses
emailRegex = re.compile(r'''
# example of the email address: some.+_thing@(\d{2,5}))?.com
[a-zA-Z0-9_.+]+             #name part
@                           # @ symbol
[a-zA-Z0-9_.+]+             #domain name part
''', re.VERBOSE)

#Step3: get the text off the clipboard
text = pyperclip.paste()

#Step4: extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

#Step5: copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
```



**Example:**

*Copy text below:*

```
Position	name 	phone	fax	email

drmr		joe		555-666-7777	123		joe@yahoo.com
asdasda		john	678-888-2222	567		asdasd@yahoo.eu
```


*Output will look like this:*

```
555-666-7777
678-888-2222
joe@yahoo.com
asdasd@yahoo.eu
```
