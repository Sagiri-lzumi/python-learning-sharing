from urllib.parse import quote
from urllib.parse import unquote
www_path = '%E5%AD%97%E8%8A%82%E5%BA%8F%E5%88%97-,%E7%BB%93%E6%9E%84%E5%8C%96%E8%A7%A3%E6%9E%90%E7%BB%93%E6%9E%9C,-%C2%B6'
www_name = '测速'
test = unquote(www_path)
test2 = quote(www_name)
print(test,'\n',test2)