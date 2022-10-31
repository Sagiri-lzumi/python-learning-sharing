import os


def count_words(filename):
    """描述该文件的单词数量"""
    try:
        with open(filename,encoding='utf-8') as f:
            story = f.read()
    except FileNotFoundError:
        print(f"the file:{filename} does not found!")
    else:
        words = story.split()
        words_num = len(words)
        print(f"the number of words are:{words_num}")



file1 = 'books/'
#file2 = 'alice.txt'
file2 = input("请输入书名:\n")
filename = file1+file2
count_words(filename)

#classfication  = words.count('person')
#print(classfication)
#用来计数