#~PythonVersion 3.3
#Author: Navdeep Dhuti
#StudentNumber: 3433216

#Code below generate answer for question::
#
import re
#Defining class
class codeCounter:
    #Defining constructor
    def __init__(self, doc):
        self.file = open(doc,'r')
        self.code_count = 0
    def match(self):
        firstline = True
        for data_fields in self.file:
            if firstline:
                firstline = False
            else:
                data_fields = data_fields.strip().split(',')
                code = data_fields[0]
                match = re.match('\w\d\d\*\w\<\w\>\d\w',code)
                if match:
                    self.code_count += 1
        self.file.close()
        return ('Number of values in the CODE field do not match the format x99*x<x>9x',self.code_count)

    


