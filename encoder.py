import difflib

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def encode(fname1, fname2):
	f = open(fname1)
	s = [x.replace("\n", "`").replace("-", "~") for x in f.read().split(" ")]
#	print(s)

	f2 = open(fname2)
	s2 = [x.replace("\n", "`").replace("-", "~") for x in f2.read().split(" ")]
#	print(s2)

	f3 = open("revision", "a")

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
	f.close()
	f2.close()
	f3.close()

#Main function
flag = 1
while(True):
	print("1. Add revisions")
	print("2. Clean revision file")
	choice = int(input("Select an operation: "))
	if choice == 1:
#		fname1 =  input("Enter path of Original file: ")
		fname1 = "article.txt"
		fname2 =  input("Enter path of Edited file: ")
		encode(fname1, fname2)	
		f_tmp = open("revision")
		print("Contents of revision file")
		print(f_tmp.read())
		f_tmp.close()
	else:
		f_tmp = open("revision", "w")
		f_tmp.write("")
		f_tmp.close()
