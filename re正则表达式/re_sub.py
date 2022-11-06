import re 

phone = "12132323323 #电话号码"

#删除字符串

print(re.sub(r'#.*$',"",phone))


#删除数字

print(re.sub(r'\D',"",phone))