import sys  # Atom runner needs this to output non-ASCII code with Python.
import io   # Atom runner needs this to output non-ASCII code with Python.
import os
import fnmatch

from bs4 import BeautifulSoup # Text parsing, Remember to config Python Environment/Path with Atom Runner.
from colorama import Fore, Back, Style # Print with color, debug useful.
print(sys.version) # to check python Environment.


# A function that return Boolean of Arg2 in Arg1, Both string. list.remove doesn't work
def isFound(text, find):
    return find in text


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
# print ("ß, ä, ö, ü, ¾") just a test

txtFile=[]
for txt in os.listdir('.'):
    if fnmatch.fnmatch(txt, '*.txt'):
        txtFile.append(txt)
print(txtFile)

for f in txtFile:
    content=open(f,'r', encoding='utf-8')
    noTag=[]
    for line in content.readlines():
        soup = BeautifulSoup(line, 'html.parser')
        noTag.append(soup.get_text())
        # soup.i.get_text()
    content.close()

    print(len(noTag), 'lines with no tags')

    # Replace founded text, list.remove doesn't work
    for i in noTag:
        if isFound(i,'default')==True:
            noTag[noTag.index(i)]='' # '' will be taken out latter
    print(len(noTag), 'lines contain "default" been taken out')

    for i in noTag:
        if i=='' or i=='\n':
            noTag.remove(i)
    print(len(noTag), 'lines with no tags, no empty line')

    k=open(f[:-4]+'noTag.txt', 'w', encoding='utf-8')
    for i in noTag:
        k.write(i)

    k.close()











# space
