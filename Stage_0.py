#Author: Navdeep Dhuti
#Std_id:3433216
import re
from collections import Counter
while True:
    try:# trying to open document
        doc_input = input('Enter file name:')
        doc = open(doc_input+'.csv','r')
        break
    except FileNotFoundError:#if file not found
        print("File Not Found!!")#give output

############### Variables used to store values form csv file
code_count = 0
width_count = 0
width_cond_sum = 0
sell_count = 0
numofvotes = 0
sumofvotes = 0
vegLetter_list = []
cnt = Counter()
least_elem_count = 0
numofheight = 0
sumofheight = 0
votes_or_width_count = 0
################
firstline = True# first line of the document
for data_fields in doc:
    if firstline:#if it is first line
        firstline = False# change it to false program will not read it
    else:
        data_fields = data_fields.strip().split(',')# stripping and spliting data by , sign
        code = data_fields[0]
        width = int(data_fields[1])#changing value of column 0 to int
        action = data_fields[2]
        veg = data_fields[3]
        votes = int(data_fields[4])#changing value of column 0 to int
        height = float(data_fields[5])#changing value of column 0 to float
        if votes >= 1347 and votes <= 2878:
            numofvotes += 1
            sumofvotes += votes
        if height >= 1.75 and height <= 2.48:
            numofheight += 1
            sumofheight += height
        match = re.match('\w\d\d\*\w\<\w\>\d\w',code)#matching the code
        if match:
            code_count += 1
        width_count += 1
        if width < 21:
            width_cond_sum += width_count
        if 'sell' in action:
            sell_count += 1
        if votes < 1653 or width < 13:
            votes_or_width_count += 1        
        cnt[veg] += 1
cnt_dict = dict(cnt)
x = min(cnt_dict.values())
for least_elem in cnt_dict.values():#Loop to find the least element in the dictionary
    if least_elem == x:#if the count of least element in the dictionary matches x
        least_elem_count += 1#Add 1 to the least_elem_count variable
average_votes = sumofvotes//numofvotes
average_height = numofheight/sumofheight

#whole output
#################################################################################################################################
print('Number of matched code == %d'%(code_count))
print('The number of (sell) in the field [action] == %d'%(sell_count))
print('Sum of the values in the field [width] less than (21) == %d'%(width_cond_sum))
print('The lines where votes is less than 1653 *or* width is less than 13 == %d'%(votes_or_width_count))
print('The average value of the numbers in field [votes] in the range (1347) and (2878) inclusive == %d'%(average_votes))
print('The average value of the numbers in the field [height] in the range (1.75) and (2.48) inclusive == %f'%(average_height))
print('The least common string appear %d time in the field [veg]'%(least_elem_count))
print('-'*40,'The End','-'*32)
##################################################################################################################################
