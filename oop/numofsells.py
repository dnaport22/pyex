#~PythonVersion 3.3
#Author: Navdeep Dhuti
#StudentNumber: 3433216

#Code below generate answer for question::

class numofSells:
    def __init__(self, doc):
        self.file = open(doc,'r')
        self.sell_count = 0
    def NumofSells(self):
        firstline = True
        for data_fields in self.file:
            if firstline:
                firstline = False
            else:
                data_fields = data_fields.strip().split(',')
                action = data_fields[2]
                if 'sell' in action:
                    self.sell_count += 1
        self.file.close()
        return ('Number of (sells) in the field [action]',self.sell_count)
    
