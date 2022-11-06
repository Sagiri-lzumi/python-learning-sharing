import re

num = '1023200'

print(re.match(r'(\d+)(0*)$',num).groups())

print(re.match(r'(\d+?)(0*)$',num).groups())
