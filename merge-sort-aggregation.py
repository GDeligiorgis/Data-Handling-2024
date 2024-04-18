#GEORGIOS DELIGIORGIS AM:4662#
import sys
import csv
import math

def merge(input_list, start, l, r):
    global grouping , aggr , func
    left_list = l
    right_list = r
    i = j = 0
    k = start
    while i < len(left_list) and j < len(right_list):#go through both lists and sort them according to the grouping attribute
        if int(left_list[i][grouping]) <= int(right_list[j][grouping]):
            input_list[k] = left_list[i]
            i+=1
        else:
            input_list[k] = right_list[j]
            j += 1
        k += 1
    #if one of them finishes first just append the remaining values of the other list
    while i < len(left_list):
        input_list[k]=left_list[i]
        k+=1
        i += 1
    while j < len(right_list):
        input_list[k]=right_list[j]
        j += 1
        k+=1
        
#split the list reccursively to sublists until it is not possible (start=end)       
def split(input_list, start, end):
    if start < end:
        mid = math.floor((start + end)/2)
        split(input_list, start, mid)
        split(input_list, mid + 1, end)
        #create 2 separate lists and sort/merge them according to the grouping attribute
        split_left=input_list[start:mid + 1]
        split_right=input_list[mid + 1:end + 1]
        merge(input_list, start, split_left, split_right)
       
#get the file [1] , grouping attribute [2] , aggregation attribute [3] and function attribute [4]
file_csv=open(sys.argv[1],'r')
grouping= int(sys.argv[2])
aggr=int(sys.argv[3])
func=sys.argv[4]
#open a file to write the result of the merge sort with aggregation
output_csv = open('O1.csv',mode='w' ,newline='') 
writerO=csv.writer(output_csv)
#make input file as list load to memory and split it 
entry=csv.reader(file_csv)
entry_list=list(entry)
list_start=0
list_end=len(entry_list)-1
#for item in entry_list:
#    print(item)
split(entry_list, list_start, list_end)
#for item in entry_list:
#    print(item)
current_group = None
current_agg = None
sum_agg_val=0  
#parse through sorted list and apply fucntion to the aggragation attribute
for item in entry_list:
    next_group=item[grouping]
    next_agg=int(item[aggr])
    if current_group is None:
        current_group = item[grouping]
        current_agg = item[aggr]
        sum_agg_val+=int(current_agg)
    elif next_group == current_group:
        if func=='max':
            current_agg = max(int(current_agg), int(item[aggr]))
        elif func=='min':
            current_agg = min(int(current_agg), int(item[aggr]))
        else:#case of sum 
            if current_group == next_group:
                sum_agg_val+= next_agg
            current_agg=sum_agg_val
    else:#nextgroup != current group function (max,min,sum) ends
        writerO.writerow([current_group] + [current_agg])#write group and aggr atribute to out file
        current_group =next_group#move to the next group
        current_agg = next_agg
        sum_agg_val=current_agg#if sum set sum_agg_val to zero 
if current_group is not None:
    writerO.writerow([current_group] + [current_agg])
    