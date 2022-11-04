
import re 
s = "asdfjvjadsffvaadfkfasaffdsasdffadsafafsafdadsfaafd"
 
ret = re.findall(r'(af)' , s)
print(len(ret))