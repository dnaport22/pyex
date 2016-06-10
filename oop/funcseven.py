#~PythonVersion 3.3
#Author: Navdeep Dhuti
#StudentNumber: 3433216

#Code below generate answer for question::
#
class funcSeven:
    def __init__(self, doc):
        self.file = open(doc,'r')
        self.votes_or_width_count = 0
    def func_seven(self):
        firstline = True
        for data_fields in self.file:
            if firstline:
                firstline = False
            else:
                data_fields = data_fields.strip().split(',')
                width = int(data_fields[1])
                votes = int(data_fields[4])
                if votes < 1653 or width < 13:
                        self.votes_or_width_count += 1
        self.file.close()
        return ('Number of lines where votes is less than 1653 *or* width is less than 13',self.votes_or_width_count)
    
                     

