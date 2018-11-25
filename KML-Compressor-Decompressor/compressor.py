import difflib
import xml.etree.ElementTree as ET

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def encode(str1, str2):
	output = ""
	s = [x.replace("\n", "`").replace("-", "~") for x in str1.split(" ")]

	s2 = [x.replace("\n", "`").replace("-", "~") for x in str2.split(" ")]

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

	pos = 0
	neg = 0

	for x in result:
		if x[0] == " ":
			pos += 1
			if neg != 0:
				output += "-"+str(neg)+" "
				neg = 0
		elif x[0] == "-":
			neg += 1
			if pos != 0:
				output += str(pos)+" "
				pos = 0	
		elif x[0] != "?":
			if pos != 0:
				output += str(pos)+" "
				pos = 0	
			if neg != 0:
				output += "-"+str(neg)+" "
				neg = 0
			if is_number(x[2:]):
				output += "'"+x[2:]+"' "
			else:			
				output += x[2:]+" "
	if pos != 0:
		output += str(pos)+" "
	if neg != 0:
		output += "-"+str(neg)+" "
	return output.replace("\t\t\t", "")

#Main function

file_name = input("Enter path of KML file:")

tree = ET.parse(file_name)
root = tree.getroot()
last_rev = ""
count = 0
length = len(root[0].findall('Instance'))

print(length, " revisions found")

for i in root.iter('Text'):
	count += 1
	if(count == length):
		last_rev = i.text

count = 0

for i in root.iter('Text'):
	count += 1
	if(count != length):
		tmp_str = i.text
		i.text = encode(last_rev, tmp_str)
	print("Revision ", count, " written")	

tree.write('compressed.kml')
f = open('compressed.kml')
f_str = f.read()
f.close()

f2 = open('compressed.kml', "w")
f2.write("<?xml version='1.0' encoding='utf-8'?>\n"+f_str)
f2.close()
