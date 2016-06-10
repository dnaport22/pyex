#~PythonVersion 3.3
#Author: Navdeep Dhuti
#StudentNumber: 3433216

#Code below generate answer for question::
#
from collections import Counter
class leastVeg:
    def __init__(self, doc):#initialising class
        self.file = open(doc,'r')
        self.vegLetter_list = []
        self.least_elem_count = 0
        self.cnt = Counter()
        self.cnt_dict = {}        
    def leastVegResult(self):
        firstline = True
        for data_fields in self.file:
            if firstline:
                firstline = False
            else:
                data_fields = data_fields.strip().split(',')
                veg = data_fields[3]
                self.cnt[veg] += 1
                self.cnt_dict = dict(self.cnt)
        x = min(self.cnt_dict.values())
        y = self.cnt_dict.values()
        for least_elem in y:
                if least_elem == x:
                    self.least_elem_count += 1
        self.file.close()
        return ('Number of times the least common string appear in the field [veg]',self.least_elem_count)


