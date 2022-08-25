import re

mylines = []
#pattern = re.compile(r"\bAUTO MERCADO ALAJUELA\b")
pattern = re.compile(r"(\d{2}\/\d{2}\/\d{4})(.*)\t{1,}(.*)(CRC|USD)")

with open('amex.txt', 'rt') as myfile:
    for myline in myfile:
        match = pattern.search(myline)
        if match != None:
            if match.group(4) == 'CRC':
                mylines.append("Julio_2022,"+match.group(1)+",AMEX,Otros,"+match.group(3).replace(',','').strip()+",0,"+match.group(2).strip())
            else:
                mylines.append("Julio_2022,"+match.group(1)+",AMEX,Otros,0,"+match.group(3).replace(',','').strip()+","+match.group(2).strip())


for element in mylines:
    print(element)