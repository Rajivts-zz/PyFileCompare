# PyFileCompare
A File Compare tool similar in function to windows fc 

The FileCompare tool can be used by commandline with the following syntax:
python FileCompare.py <original file path> <new file path>

Output:
a. The lines that are added in the new file which were not present in the original file
b. The lines that were in the original file but are removed in the new file
c. The lines that are both in the new and original file, yet not in the same order

#ToDo
Add support for comparing binary files, allow option for performing file compare without considering the whitespaces.
