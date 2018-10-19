import difflib

def encode(fname1, fname2):
	f = open(fname1)
	s = f.read().split()
	#print(s)

	f2 = open(fname2)
	s2 = f2.read().split()
	#print(s2)

	f3 = open("revision", "a")

	d = difflib.Differ()

	result = list(d.compare(s, s2))

	#print(result)


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
		else:
			if pos != 0:
				f3.write(str(pos)+" ")
				pos = 0	
			if neg != 0:
				f3.write("-"+str(neg)+" ")
				neg = 0
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
while(flag == 1):
	print("1. Add revisions")
	print("2. Clean revision file")
	choice = int(input("Select an operation: "))
	if choice == 1:
		fname1 = input("Enter path of original file: ")
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
	flag = int(input("Press 1 to continue or 0 to exit: "))				