import re

# Read the data
ipAddresses = []
fileHandler = open('04_Make/ipAddresses.txt', 'r')
for ip in fileHandler:
    ipAddresses.append(ip)
fileHandler.close()

# Your code starts here
ip1 = "192.256.1.1" # ungültige IPv4 -> 256 statt 255
ip2 = "224.0.0.202" # gültig IPv4

ip3 = "2001:0db8:85a3:0000:0000:8a2e:0370:7362" #gültig
ip4 = "2001:0db8:85a3:0000:0000:8a2e:0370:gggg" #ungültig
# IPv6 gültig, wenn 16bits = 0-9 und a-f (=16 Zeichen); 8 Gruppen, getrennt mit :

regv6 = re.compile("^((([0-9|[a-f])*){4}: ){7}(([0-9]|[a-f])*){4}$")

m = regv6.match(ip3)
print(m)
m = regv6.match(ip4)
print(m)



'''
for i in ipAddresses:
    reg = re.compile("^\d*\.\d*\.\d*\.\d*$")
    m = reg.match("i")
    if m != None:
        print(m)

#reg = re.compile("^\d*\.\d*\.\d*\.\d*$")
#
#m = reg.match("203.0.113.203")
#print(m)
'''
