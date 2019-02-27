import json

def set_value(key, value):
    with open(key, 'w') as file:
        json.dump(value, file)

    with open("data2/history.puff", "a") as file:
        row = key + '----' + str(value)
        file.write(row)
        file.write('\n')

def get_value(key):
    with open(key, 'r') as file:
        data = json.load(file)
    return data

def set_current_db():
    with open('data/history.puff', 'r') as file:
        for line in file.read().split('\n'):
            if line:
                key_path, value = line.split('----')
                set_value(key_path, value)

set_current_db()
# value = {'a': ['compex list'], 'b': 1}
# key = 'two'
# set_value(key, value)
# print(get_value(key))