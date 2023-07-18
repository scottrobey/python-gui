import re as regex

print('Hello, World!')

pattern = regex.compile('Wormhole code is:.*')
line = 'Wormhole code is: 82-congregate-indoors'

m = pattern.match(line)
if m:
    print("Matches!")
    print(f"Group: {m.group()}")
