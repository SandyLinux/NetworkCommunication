
import re
with open('resolv.conf','r') as fp:

    dataline = fp.read()
    print(dataline)
    gws = re.findall(r'\d+.\d+.\d+.\d+',dataline)
    print(gws)
