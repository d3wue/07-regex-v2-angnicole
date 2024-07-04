import re

# Read the data
ipAddresses = []
fileHandler = open('04_Make/ipAddresses.txt', 'r')
for ip in fileHandler:
    ipAddresses.append(ip)
fileHandler.close()

# Your code starts here


for i in ipAddresses:
    reg = re.compile("^\d*\.\d*\.\d*\.\d*$")
    m = reg.match("i")
    #if m != "None":
    print(m)


#reg = re.compile("^\d*\.\d*\.\d*\.\d*$")
#
#m = reg.match("203.0.113.203")
#print(m)