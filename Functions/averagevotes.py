#~PythonVersion 3.3
#Author: Navdeep Dhuti
#StudentNumber: 3433216

#Code below generate answer for question::
#What is the average value of the numbers in the field [votes] in the range(1347)and(2878)inclusive?



#Function starts
def Average_votes(doc_in):
       #Open the input file came from 'infile'
       doc = open(doc_in+'.csv','r') 
       #initialising variables
       firstline = True
       numofvotes = 0
       sumofvotes = 0
       #passing file into a for loop
       for data_fields in doc:
              if firstline:
                     firstline = False
              else:
                     #splitting and organising the data in file
                     data_fields = data_fields.strip().split(',')
                     #defining variable required for calculation
                     votes = int(data_fields[4])
                     if votes >= 1347 and votes <= 2878:
                            numofvotes += 1
                            sumofvotes += votes
       #calculating average
       average_votes = sumofvotes//numofvotes
       #returning average
       return (average_votes)
       #closing opened file
       doc.close()



