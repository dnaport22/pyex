#~PythonVersion 3.3
#Author: Navdeep Dhuti
#StudentNumber: 3433216

#Code below generate answer for question::
#
class widthCounter:
    def __init__(self, doc):#initialising class
        self.file = open(doc,'r') #opening document
        self.width_count = 0
        self.width_cond_sum = 0
    def Width_counter(self):
        firstline = True
        for data_fields in self.file:#passing file into a for loop
            if firstline:
                firstline = False
            else:
                data_fields = data_fields.strip().split(',')
                width = int(data_fields[1])
                self.width_count += 1
                if width < 21:
                    self.width_cond_sum += self.width_count
        self.file.close()
        return ('Sum of the values in the field [width] less than (21)',self.width_cond_sum)#giving output

