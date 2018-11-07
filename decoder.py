import xml.etree.ElementTree as ET
import xml.dom.minidom

#ET._namespace_map['http://www.mediawiki.org/xml/export-0.10/'] = ''
#ET._namespace_map['http://www.w3.org/2001/XMLSchema-instance'] = 'xsi'
tree = ET.parse('latest.kml')
root = tree.getroot()

rev = root[0].find('Instance')
root[0].remove(rev)
str1 = ET.tostring(rev).decode("utf-8")
s = str1.split(" ")

i = 0
while(True):
	if i == len(s):
		break;
	if s[i].isspace() or s[i] == '':
		del s[i]
	else:	
		i += 1	


f2 = open("revision")
tmp = f2.read().split("\n")

if len(tmp) == 1:
	print("No revisions found, generate revisions from decoder.py first")
	exit()

n = int(input(str(len(tmp)-1)+" Revisons found, enter the revision number to be loaded: "))


s2 = tmp[n-1].split()

index = 0

result = ""

for x in s2:
	if x.isdigit():
		for i in range(index, index+int(x)):
#			print(s[i], end=" ")
			result += s[i]
			result += " "
			index += 1
	elif x[0] == "'" and x[-1] == "'" and x[1:-1].isdigit():
#			print(x[1:-1].replace("`", "\n").replace("~", "-"), end=" ")				 
			result += x[1:-1].replace("`", "\n			").replace("~", "-")
			result += " "
	else:
		if x[0] == '-':
			for i in range(index, index+int(x[1:])):
				index += 1
		else:
#			print(x.replace("`", "\n").replace("~", "-"), end=" ")
			result += x.replace("`", "\n			").replace("~", "-")		
			result += " "

root[0].append(ET.fromstring(result))
tree.write('output.kml')
print(n, "th revision written to output.kml")

f = open('output.kml')
f_str = f.read()
f.close()

f2 = open('output.kml', "w")
f2.write("<?xml version='1.0' encoding='utf-8'?>\n"+f_str)
f2.close()
