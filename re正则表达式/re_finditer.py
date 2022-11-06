import re

it = re.finditer(r'\d+','adf213fda43df21fdsf2daf1243da21')

for match in it:
    print(match.group())