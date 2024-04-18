#GEORGIOS DELIGIORGIS AM:4662#
import sys
import csv

R_csv=open('R.csv','r')
S_csv=open('S.csv','r')
output_csv = open('O2.csv',mode='w' ,newline='') 

readerR=csv.reader(R_csv)
readerS=csv.reader(S_csv)
writerO=csv.writer(output_csv)

Rline=next(readerR,None)
Sline=next(readerS,None)

while Rline is not None and Sline is not None:
            if Rline[0] == Sline[1]:
                writerO.writerow([Rline[0]] + Rline[1:] + [Sline[0]] + Sline[2:])
                Sline = next(readerS, None)
            elif Rline[0] != Sline[1]:
                Rline = next(readerR, None)

