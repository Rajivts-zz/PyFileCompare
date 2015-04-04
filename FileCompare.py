from __future__ import print_function
import re
import os.path
import sys


def help():
	print("\n<<<<FILE COMPARE ROUTINE>>>")
	print("Usage:")
	print("FileCompare.py [OriginalFile] [ModifiedFile] ")

args = sys.argv

if len(args) <> 3:
	print("Incorrect number of arguments passed!")
	help()
	sys.exit(0)

file1 = args[1].encode('string-escape')
file2 = args[2].encode('string-escape')

if not os.path.isfile(file1) or not os.path.isfile(file2):
	print("Invalid file name or path. File does not exist!")
	sys.exit(0)

inp1 = open(file1, 'r')
inp2 = open(file2, 'r')

print("\n\n\n<<<<FILE COMPARE ROUTINE>>>")
#print "+++ => Line added to the new file, which was not present in the old file"
#print "--- => Line removed from the new file, which was present in the old file"
print("\n\n")

lineA = inp1.readline()
lineB = inp2.readline()

dictA, dictB = {}, {}
lineSet = set()
i, j = 1, 1

while lineA != '' or lineB != '':
	if lineA != '\n' and lineA != '':
		#print "\nLine A being considered: ", lineA
		lineSet.add(lineA)
		if lineA in dictA:
			dictA[lineA].append(i)
		else:
			dictA[lineA] = [i]
		i += 1

	if lineB !='\n' and lineB != '':
		#print "\nLine B being considered: ", lineB
		lineSet.add(lineB)
		if lineB in dictB:
			dictB[lineB].append(j)
		else:
			dictB[lineB] = [j]
		j += 1
	i = (i + 1 if lineA == '\n' else i)
	j = (j + 1 if lineB == '\n' else j)
	lineA = inp1.readline()
	lineB = inp2.readline()	


#print '\n', dictA, '\n'
#print dictB
#print '\n', lineSet, '\n'
for line in lineSet:
	numbA = (dictA[line] if line in dictA else None)
	numbB = (dictB[line] if line in dictB else None)
	
	if not numbA:			
		for elem in numbB:
			print("The line '", line.strip(), "' was added in the new file at line number <<", elem, ">> which was not present in the original file", sep='')
		continue

	elif not numbB:
		for elem in numbA:
			print("The line '", line.strip(), "' present at line number <<", elem, ">> in the original file was removed in the new file", sep='')
		continue

	if not (set(numbA) & set(numbB)):		
		sub = list(set(numbA) - set(numbB))
		add = list(set(numbB) - set(numbA))

		if add and sub:
			print("The line '", line.strip(), "' present at line number(s) ", sub, " in the original file has been shifted to line number(s) ", add, " in the new file", sep='')
		elif sub:
			for elem in sub:
				print("The line '", line.strip(), "' present at line number <<", elem, ">> in the original file was removed in the new file", sep='')

		elif add:
			for elem in add:
				print("The line '", line.strip(), "' was added in the new file at line number <<", elem, ">> which was not present in the original file", sep='')

	if set(numbA) & set(numbB) and set(numbA) ^ set(numbB):
		print("The line '", line.strip(), "' present at line number(s) ", list(set(numbA) - set(numbB)), " in the original file has been shifted to line number(s) ", list(set(numbB) - set(numbA)), " in the new file", sep='')		






