#~PythonVersion 3.3
#Author: Navdeep Dhuti
#StudentNumber: 3433216

#Code below generate answer for question::
#How many times does the least common string appear in the field [veg]?

#Importing required files/modules
from collections import Counter #To count the matching strings in the list


#Function starts
def Leastveg(doc_in):
    #Open the input file came from 'infile'
    doc = open(doc_in+'.csv','r')
    #initialising variables
    firstline = True
    vegLetter_list = []
    least_elem_count = 0
    cnt = Counter()
    #passing file into a for loop
    for data_fields in doc:
            if firstline:
                firstline = False
            else:
                #splitting and organising the data in file
                data_fields = data_fields.strip().split(',')
                #defining variable required for calculation
                veg = data_fields[3]
                #Add 1 each time when there is a same string in the list
                cnt[veg] += 1
                #Add the results to dictionary
                cnt_dict = dict(cnt)
    #Find the minimum value in the dictionary
    x = min(cnt_dict.values())
    #Loop to find the least element in the dictionary
    for least_elem in cnt_dict.values():
        #if the count of least element in the dictionary matches x
        if least_elem == x:
            #Add 1 to the least_elem_count variable
            least_elem_count += 1
    #Return the the variable holding least common string
    return(least_elem_count)    
    doc.close()            
   
