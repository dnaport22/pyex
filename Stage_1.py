#~PythonVersion 3.3
#Author: Navdeep Dhuti
#StudentNumber: 3433216

#Importing functions from files

from Functions.codecounter import Code_counter
from Functions.widthcounter import Width_counter
from Functions.numofsells import NumofSells
from Functions.leastveg import Leastveg
from Functions.averagevotes import Average_votes
from Functions.averageheight import Average_height
from Functions.funcseven import func_seven

while True:#
    try:#try to open the file
        doc_in = input('Enter file name:')
        doc = open(doc_in+'.csv')
        doc.close()
        #printing out all functions which are placed in sepaarete files
        ################################################################
        print('Number of matched code = ',Code_counter(doc_in))
        print('Sum of the values in the field [width] less than (21) = ',Width_counter(doc_in))
        print('The number of (sell) in the field [action] = ',NumofSells(doc_in))
        print('The least common string appear %d time in the field [veg] = ',Leastveg(doc_in))
        print('The average value of the numbers in field [votes] in the range (1347) and (2878) inclusive = ',Average_votes(doc_in))
        print('The average value of the numbers in the field [height] in the range (1.75) and (2.48) inclusive = ',Average_height(doc_in))
        print('The lines where votes is less than 1653 *or* width is less than 13 = ',func_seven(doc_in))
        break
    except FileNotFoundError:#otherwise file was not found and give error
        print("File Not Found!!")
