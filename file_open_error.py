file_name = 'alice.txt'

try:
    with open(file_name,encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print(f"the file:{file_name} does not exist")