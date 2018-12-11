# (700)-707-0902 torgox@icloud.com
# (758)-740-2268 naoya@hotmail.com
# (404)-692-7383 martyloo@hotmail.com
# 980-958-9813 mrsam@att.net
# (843)-684-7966 mastinfo@live.com
# (645)-687-1570 muadi_p@sbcglobal.net
# (269)-878-3326 shazow@icloud.com
# (720)-236-1287 seemant@sbcglobal.net
# (559)-211-7456 lstein@icloud.com
# (338)-610-3129 fraser@me.com 

#Create a regex for phone numbers

#Examples
#415-654-3446, 555-5555, (415) 555-7645, 654-5555 ext 12345, ext.54367, x123

import pyperclip, re

phoneRegex = re.compile(r'''
(
((\d\d\d) | (\(\d\d\d\)))?			#area code (optional)
(\s|-)			#first separator
\d\d\d			#first 3 digits
-				#second separator
\d\d\d\d		#last 4 digits
(((ext(\.)?\s)|x) #extension word part
(\d{2,5}))?			#extension number part
)


''', re.VERBOSE)

# Create a regex for email addresses



emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+ # name part
@ #@ symbol
[a-zA-Z0-9_.+]+#domain name part

''',re.VERBOSE)
# Get the text off of the clipboard

text = pyperclip.paste()


# Extract the email/phone from this text

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

# copy the extracted email/phone to clipboard

allPhoneNumbers = []
for phoneNumber in extractedPhone:
	allPhoneNumbers.append(phoneNumber[0])


# '\n'.join will separate each item in the list by the \n 
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)

pyperclip.copy(results)















