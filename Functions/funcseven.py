#~PythonVersion 3.3
#Author: Navdeep Dhuti
#StudentNumber: 3433216

#Code below generate answer for question::
#count the lines where votes is less than 1653 *or* width is less than 13



#Function starts
def func_seven(doc_in):
    #Open the input file came from 'infile'
    doc = open(doc_in+'.csv','r')
    #initialising variables
    firstline = True
    votes_or_width_count = 0
    for data_fields in doc:
            if firstline:
                firstline = False
            else:
                #splitting and organising the data in file
                data_fields = data_fields.strip().split(',')
                #defining variable required for calculation
                width = int(data_fields[1])
                votes = int(data_fields[4])
                #counting the lines as according to the question 
                if votes < 1653 or width < 13:
                        votes_or_width_count += 1
    return votes_or_width_count
    #closing opened file
    doc.close()
                     

