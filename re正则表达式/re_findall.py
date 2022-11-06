
import re 
s = "asdfjvjadsffvaadfkfasaffdsasdffadsafafsafdadsfaafd happy"
 
ret = re.findall(r'\bha[a-z]*' , s) #匹配的是单词的边界是ha加上[a-z]的字母以及*（后续任意个数的字符）
print(len(ret))
print(ret)

#secondary
scheme = re.compile(r'\bha[a-z]*')
ret2 = scheme.findall('a happy happpppp sss',1,20)
print(ret2)