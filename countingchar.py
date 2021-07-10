import pprint, pyperclip

#copy the enter text you want to scan
userString = pyperclip.paste()

#create a empty dictionary to story all the char values
count = {}

for char in userString.upper(): #using upper case to convert all the letters to captials
    count.setdefault(char, 0)
    count[char] = count[char]+1

#using pprint to print the output understandable
pprint.pprint(count)
