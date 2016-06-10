#~PythonVersion 3.3
#Author: Navdeep Dhuti
#StudentNumber: 3433216

#Code below generate answer for question::
#What is the average value of the numbers in the field [height] in the range(1.75)and(2.48)inclusive?

#Defining class
class averageHeight:
    #Defining constructor
    def __init__(self, doc):
        self.file = open(doc,'r')
        self.numofheight = 0
        self.sumofheight = 0
    def average(self):
        firstline = True
        for data_fields in self.file:
            if firstline:
                firstline = False
            else:
                data_fields = data_fields.strip().split(',')
                height = float(data_fields[5])
                if height >= 1.75 and height <= 2.48:
                    self.numofheight += 1
                    self.sumofheight += height
        self.file.close()
        average_height = self.numofheight/self.sumofheight
        return ('Average value of the numbers in the field [height] in the range (1.75) and (2.48) inclusive',float(average_height))
