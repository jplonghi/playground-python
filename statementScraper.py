import re

mylines = []
pattern = re.compile(r"\bJAPAN TICO\b")
with open('demofile.txt', 'rt') as myfile:
    for myline in myfile:
        if pattern.search(myline) != None:
            mylines.append(myline.rstrip('\n'))


for element in mylines:
    print(element)