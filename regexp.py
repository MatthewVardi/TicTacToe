import re

message = 'Call me at 415-555-0987 tomorrow or at 516-582-4444 for my office line'

#we pass in a raw string
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex.findall()(message))
