my_list = ['geeks', 'for', 'geeks']

def convert(list):
    res = str(",".join(map(str, list)))
    return res

print(convert(my_list))