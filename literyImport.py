import os
import re

printFiles = False;
printImports = True;

dirPath = '/Users/chiehchun/Desktop/project/xiami8.0/newxiami/LocalPods/UserSystem/';
importLines = [];

def main():
	importStrings = loopFileImports(dirPath);
	seperator = '\n';
	if printFiles:
		print(seperator.join(importStrings));
	if printImports:
		importLines.sort();
		print(seperator.join(importLines));


def loopFileImports( path ): #return [String]
	importStrings = [];
	for filename in os.listdir(path):
	    if filename.endswith(".m") or filename.endswith(".h"): 
	         # print(os.path.join(directory, filename))
	    	# print('file : '+filename);
	    	importStrings.append(filename);
	    	readLinesContainsImports(path+filename);
	        continue;
	    else:
	    	if (isFile(path + filename)):
				importStrings.extend(loopFileImports(path + filename + '/'));
	        continue;
	return importStrings;

def isFile( path ): #return BOOLEAN
	if os.path.isdir(path): 
		# print('It is a directory :' + path);
		return True
	# elif (os.path.isfile(path)):
		# print('\n it is a normal file');
	# else:
		# print('other files');
	return False;

def readLinesContainsImports( fileName ): 
	opener = open(fileName, "r");
	for line in opener:
		if re.match("#import (.*)", line):
			if any(line in lines for lines in importLines) == False:
				importLines.append(line);


if __name__ == "__main__":
    main();

