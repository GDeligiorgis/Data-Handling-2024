#GEORGIOS DELIGIORGIS AM:4662#
import sys
import csv

arguments = sys.argv[1:]

#print("Arguments:", arguments)
#here we initialize the reading files we use as input and the writing file we use as output
#R_csv=open(sys.argv[1],'r')
#S_csv=open(sys.argv[2],'r')
R_csv=open('R.csv','r')
S_csv=open('S.csv','r')
output_csv = open('O3.csv',mode='w' ,newline='') 

readerR=csv.reader(R_csv)
readerS=csv.reader(S_csv)
writerO=csv.writer(output_csv)

Rline=next(readerR,None)
Sline=next(readerS,None)
SumSE=0

while Rline is not None and Sline is not None:
    if Rline[0] == Sline[1]:
        if Rline[2]=='7':
            while Rline[0]==Sline[1] :
                SumSE+=int(Sline[2])
                SA=Sline[1]
                Sline = next(readerS, None)
            writerO.writerow([SA] + [SumSE])
            SumSE=0 
        elif Rline[2]!='7':
            Sline = next(readerS, None)
    else :
        Rline = next(readerR, None)
   


