import re

import pandas as pd


def get_lines(file):
    
    with open(file, 'r') as f:
        lines = f.readlines()
        f.close()
    return lines


def strip_newline(string):
    
    stripped_string = []

    for item in string:
        strip = re.sub('\n', '', item)
        stripped_string.append(strip)

    return stripped_string

def strip_key(string):
    
    regex = re.compile(r'\s+:')
    strip = re.sub(regex, '', string)
    
    return strip


def strip_value(string):
    # regex = re.compile(r':\s+')
    strip = re.sub(r'\s+:\s+', '', string)
    #print(strip)
    return strip


##### Function Starts here #####
file_path = "test.txt"
lines = get_lines(file_path)
lines_stripped = strip_newline(lines)

data = {}
regex = re.compile('(\w+\s+:)')
for item in lines_stripped:
    
    search = re.search(regex, item)   
    key_extract = search.group()
    key = strip_key(key_extract)
    start_index = len(key)
    value = item[start_index:]
    
    value_stripped = strip_value(value)
    
    data[key] = value_stripped

    
df = pd.DataFrame([data.values()], columns=data.keys())

df.to_csv('out.csv', index=False)

print(data)