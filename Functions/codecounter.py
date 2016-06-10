#~PythonVersion 3.3
#Author: Navdeep Dhuti
#StudentNumber: 3433216

#Code below generate answer for question::
#How many values in the 'code' field do not match the format x99*x<x>9x?


#Importing required files/modules
import re


#Function starts
def Code_counter(doc_in):
    #Open the input file came from 'infile'
    doc = open(doc_in+'.csv','r')
    #initialising variables
    code_count = 0
    firstline = True
    #passing file into a for loop
    for data_fields in doc:
            if firstline:
                firstline = False
            else:
                #splitting and organising the data in file
                data_fields = data_fields.strip().split(',')
                code = data_fields[0]
                match = re.match('\w\d\d\*\w\<\w\>\d\w',code)
                if match:
                    code_count += 1
    #returning the times code matched                
    return code_count
    #closing opened file
    doc.close()



