import difflib
import xml.etree.ElementTree as ET

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def encode(str1, str2, f3):
	s = [x.replace("\n", "`").replace("-", "~") for x in str1.split(" ")]
#	print(s)

	s2 = [x.replace("\n", "`").replace("-", "~") for x in str2.split(" ")]
#	print(s2)
	i = 0
	while(True):
		if i == len(s):
			break;
		if s[i].isspace() or s[i] == '':
			del s[i]
		else:	
			i += 1	
	i = 0
	while(True):
		if i == len(s2):
			break;
		if s2[i].isspace() or s2[i] == '':
			del s2[i]
		else:	
			i += 1	
			
	d = difflib.Differ()

	result = list(d.compare(s, s2))

#	print(result)
	pos = 0
	neg = 0

	for x in result:
		if x[0] == " ":
			pos += 1
			if neg != 0:
				f3.write("-"+str(neg)+" ")
				neg = 0
		elif x[0] == "-":
			neg += 1
			if pos != 0:
				f3.write(str(pos)+" ")
				pos = 0	
		elif x[0] != "?":
			if pos != 0:
				f3.write(str(pos)+" ")
				pos = 0	
			if neg != 0:
				f3.write("-"+str(neg)+" ")
				neg = 0
			if is_number(x[2:]):
				f3.write("'"+x[2:]+"' ")
			else:			
				f3.write(x[2:]+" ")
	if pos != 0:
		f3.write(str(pos)+" ")
	if neg != 0:
		f3.write("-"+str(neg)+" ")
	f3.write("\n")

#Main function

#Parsing
ET._namespace_map['http://www.mediawiki.org/xml/export-0.10/'] = ''
ET._namespace_map['http://www.w3.org/2001/XMLSchema-instance'] = 'xsi'
tree = ET.parse('Indian Institute of Technology Ropar.xml')
root = tree.getroot()

count = 1
str1 = " "
str_array = []
length = len(root[1].findall('{http://www.mediawiki.org/xml/export-0.10/}revision'))

for i in root[1].findall('{http://www.mediawiki.org/xml/export-0.10/}revision'):
	if count == length:
		str1 = ET.tostring(i).decode("utf-8")
	else:
		str_array.append(ET.tostring(i).decode("utf-8"))			
	root[1].remove(i)
	count += 1

root[1].append(ET.fromstring(str1))
tree.write('latest.xml')

#write revision one by one to revision file
f3 = open("revision", "w")

count = 0
for str2 in str_array:
	encode(str1, str2, f3)
	count += 1
	print("Revision ", count, " written")	

f3.close()
