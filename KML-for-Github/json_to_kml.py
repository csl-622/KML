import dicttoxml
from xml.dom.minidom import parseString
import xml.etree.ElementTree as ET
import json

f = open("dummy1.json")
d1 = json.load(f)
f.close()

f = open("dummy2.json")
d2 = json.load(f)
f.close()

d = []

for (x, y) in zip(d1, d2):
	z = {}
	tmp_str = str(str(y["dictionary"]).encode('utf-8'))
	z["body"] = tmp_str[tmp_str.find("{"):tmp_str.rfind("}")+1]
	tmp = {**x, **z}
	d.append(tmp)

D = {}
D["KnowledgeData"] = d

DD = {}
DD["KML"] = D

my_item_func = lambda x: 'Instance'

xml = dicttoxml.dicttoxml(DD, attr_type=False, root=False, item_func=my_item_func)

dom = parseString(xml)

f = open("sample_output.kml", "w")

kml_str = str(dom.toprettyxml())

f.write(kml_str)
f.close()
print("sample_output.kml created")

tree = ET.parse('sample_output.kml')
root = tree.getroot()

for i in root.iter('TimeStamp'):
	tmp = ET.Element('CreationDate')
	tmp.text = i.text
	i.text = ""
	i.append(tmp)

for i in root.iter('Contributors'):
	tmp = ET.Element('LastEditorUserName')
	tmp2 = ET.Element('LastEditorUserId')
	tmp.text = i.text
	tmp2.text = i.text+"@github.com"
	i.text = ""
	i.append(tmp)
	i.append(tmp2)

for i in root.iter('body'):
	tmp = ET.Element('Test')
	tmp.text = i.text
	tmp.set("Type", "github/json")
	i.text = ""
	i.append(tmp)

count = 1

for i in root.iter('Instance'):
	i.set("Id", str(count))
	i.set("Type", "github/json")
	count += 1

root[0].set("Type", "unknown")	

tree.write('sample_output.kml')

f = open('sample_output.kml')
f_str = f.read()
f.close()

f2 = open('sample_output.kml', "w")
f2.write("<?xml version='1.0' encoding='utf-8'?>\n"+f_str.replace("></", ">\n\t\t\t</").replace("><", ">\n\t\t\t\t<"))
f2.close()
