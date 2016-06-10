#~PythonVersion 3.3
#Author: Navdeep Dhuti
#StudentNumber: 3433216

#Code below generate answer for question::
#What is the average value of the numbers in the field [height] in the range(1.75)and(2.48)inclusive?


#Function starts
def Average_height(doc_in):
    doc = open(doc_in+'.csv','r') #Open the input file came from 'infile'
    #initialise variables
    firstline = True
    numofheight = 0
    sumofheight = 0
    #passing file into a for loop
    for data_fields in doc:
            if firstline:
                firstline = False
            else:
                #splitting and organising the data in file
                data_fields = data_fields.strip().split(',')
                #defining variable required for calculation
                height = float(data_fields[5])
                if height >= 1.75 and height <= 2.48:
                    numofheight += 1
                    sumofheight += height
    #calculating average
    average_height = numofheight/sumofheight
    #rturning average
    return ('%f'%average_height)
    #closing opened file
    doc.close()

