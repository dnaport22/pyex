#~PythonVersion 3.3
#Author: Navdeep Dhuti
#StudentNumber: 3433216

#Code below generate answer for question::

from oop.codecount import *
from oop.leastveg import *
from oop.averageheight import *
from oop.widthcounter import *
from oop.averagevotes import *
from oop.funcseven import *
from oop.numofsells import *

while True:
    try:
        doc_in = input('Enter file name:')
        file = open(doc_in+'.csv')
        file.close()
        code = codeCounter(doc_in+'.csv')
        veg = leastVeg(doc_in+'.csv')
        ave_height = averageHeight(doc_in+'.csv')
        width = widthCounter(doc_in+'.csv')
        ave_votes = averageVotes(doc_in+'.csv')
        seven = funcSeven(doc_in+'.csv')
        sells = numofSells(doc_in+'.csv')
        print(code.match())
        print(veg.leastVegResult())
        print(ave_height.average())
        print(width.Width_counter())
        print(ave_votes.Average_votes())
        print(seven.func_seven())
        print(sells.NumofSells())
        break
    except FileNotFoundError:
        print("File Not Found!!")
        
