f = open("article.txt")
s = f.read().split()

f2 = open("revision")
tmp = f2.read().split("\n")

if len(tmp) == 1:
	print("No revisions found, generate revisions from decoder.py first")
	exit()

n = int(input(str(len(tmp)-1)+" Revisons found, enter the revision number to be loaded: "))


s2 = tmp[n-1].split()

index = 0

for x in s2:
	if x.isdigit():
		for i in range(index, index+int(x)):
			print(s[i], end=" ")
			index += 1
	else:
		if x[0] == '-':
			for i in range(index, index+int(x[1:])):
				index += 1
		else:
			print(x, end=" ")		
print("")				
