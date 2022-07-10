'''
Python Regular Regression: are extremely useful in extracting information from text
such as code, log files, spreadsheets, or even documents. 
- The re module allow search a string for a match:
    + findall(): return a list containing all matches
    + search(): return a MatchObject if there is a match anywhere in the string
        MatchObject contains: span(), string(), group()
    + split(): return a list where the string has been split at each match
    + sub(): replaces one or many matches with a string
'''
import re
text = "Hello Luat, I am a AI am computer."

# findall method
# a = re.findall("am", text)
# print(len(a))
# print(a)

# search() method
b = re.search("am", text)
print(b)
print(b.span())
print(b.string)
print(b.group())

