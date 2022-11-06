import re
if re.match('www','www.baodu.com'):
    print("allowed")

print(re.match('www','www.baodu.com.www'))

# match('compare','origional','else')
