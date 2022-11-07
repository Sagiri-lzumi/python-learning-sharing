import re 

phone = "12132323323 #电话号码"

#删除字符串

print(re.sub(r'#.*$',"替换的内容",phone))


#删除数字

print(re.sub(r'\D',"替换的内容",phone))