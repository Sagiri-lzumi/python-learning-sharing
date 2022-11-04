import re 
 
s = "955423423"
ret = re.match(r'[1-9]\d{4,9}$' , s)
if ret != None:
    print(ret.group(),"congrulations!")
else :
    print('匹配失败!')