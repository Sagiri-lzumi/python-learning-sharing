import urllib.parse

www = "https://blog.csdn.net/whatday/article/details/107746381"
spilt = urllib.parse.urlparse(www)

print(spilt)