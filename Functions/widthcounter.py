#~PythonVersion 3.3
#Author: Navdeep Dhuti
#StudentNumber: 3433216

#Code below generate answer for question::
#Find the sum of the values in the field [width] less than (21)



def Width_counter(doc_in):
    #Open the input file came from 'infile'
    doc = open(doc_in+'.csv','r')
    #initialising variables
    width_count = 0
    width_cond_sum = 0
    firstline = True
    #passing file into a for loop
    for data_fields in doc:
            if firstline:
                    firstline = False
            else:
                    data_fields = data_fields.strip().split(',')
                    width = int(data_fields[1])
                    width_count += 1
                    if width < 21:
                        width_cond_sum += width_count
    return(width_cond_sum)

