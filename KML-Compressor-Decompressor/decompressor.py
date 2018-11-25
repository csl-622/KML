import xml.etree.ElementTree as ET
import xml.dom.minidom

file_name = input("Enter compressed KML file path: ")

tree = ET.parse(file_name)
root = tree.getroot()
last_rev = ""
count = 0
length = len(root[0].findall('Instance'))

for i in root.iter('Text'):
	count += 1
	if(count == length):
		last_rev = i.text

s = last_rev.split(" ")

i = 0
while(True):
	if i == len(s):
		break;
	if s[i].isspace() or s[i] == '':
		del s[i]
	else:	
		i += 1	


if length == 1:
	print("No revisions found, generate revisions from encoder.py first")
	exit()

n = int(input(str(length)+" Revisons found, enter the revision number to be loaded: "))

asked_rev = " "

count = 0

for i in root.iter('Text'):
	count += 1
	if(count == n):
		asked_rev = i.text

s2 = asked_rev.split(" ")

i = 0
while(True):
	if i == len(s2):
		break;
	if s2[i].isspace() or s2[i] == '':
		del s2[i]
	else:	
		i += 1	

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

count = 0

for i in root[0].findall('Instance'):
	count += 1
	if count == n:
		i[4][0].text = result
	else:
		root[0].remove(i)

tree.write('output.kml')
print(n, "th revision written to output.kml")

f = open('output.kml')
f_str = f.read()
f.close()

f2 = open('output.kml', "w")
f2.write("<?xml version='1.0' encoding='utf-8'?>\n"+f_str)
f2.close()
