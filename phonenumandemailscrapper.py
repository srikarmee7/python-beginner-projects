import re, pyperclip #import regular expression and pyperclip module

script = pyperclip.paste()  # This is a input string, copy the text to find phone numbers.

phone_regex = re.compile(r'(\d\d\d\d\d\d\d\d\d\d)') #pattern to find typical 10digit phone number
email_regex = re.compile(r'''(
#([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)

[a-zA-Z0-9_.+]+ #first part
@[a-zA-Z0-9_.+]+ #@ symbol
\.[a-zA-Z0-9_-]+ #domain name part

)''',re.VERBOSE)

phoneNums = phone_regex.findall(script) #using findall method to find all the numbers
print("Phone numbers found are: ")
print('\n'.join(str(nums) for nums in phoneNums)) #using join method for to print numbers in serial order.

emails = email_regex.findall(script)  #using findall method to find emails in copied text
print("These are the email's found in the copied text: ")
print('\n'.join(str(e) for e in emails))