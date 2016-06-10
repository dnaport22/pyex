#~PythonVersion 3.3
#Author: Navdeep Dhuti
#StudentNumber: 3433216

#Code below generate answer for question::
#Count the number of (sell's) in the field [action]



#Function starts
def NumofSells(doc_in):
    #Open the input file came from 'infile'
    doc = open(doc_in+'.csv','r')
    #initialising variables
    sell_count = 0
    firstline = True
    #passing file into a for loop
    for data_fields in doc:
            if firstline:
                    firstline = False
            else:
                    data_fields = data_fields.strip().split(',')
                    action = data_fields[2]
                    if 'sell' in action:
                        sell_count += 1
    return sell_count
    doc.close()
