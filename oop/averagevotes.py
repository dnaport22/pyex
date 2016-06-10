#~PythonVersion 3.3
#Author: Navdeep Dhuti
#StudentNumber: 3433216

#Code below generate answer for question::
#What is the average value of the numbers in the field [votes] in the range(1347)and(2878)inclusive?

#Defining Class
class averageVotes:
       #Defining Constructor
       def __init__(self, doc):
              self.file = open(doc,'r')
              self.numofvotes = 0
              self.sumofvotes = 0
       #Defining Method
       def Average_votes(self):
              firstline = True
              for data_fields in self.file:
                     if firstline:
                            firstline = False
                     else:
                            data_fields = data_fields.strip().split(',')
                            votes = int(data_fields[4])
                            if votes >= 1347 and votes <= 2878:
                                   self.numofvotes += 1
                                   self.sumofvotes += votes
              self.file.close()
              average_votes = self.sumofvotes//self.numofvotes
              return ('Average value of the numbers in the field [votes] in the range (1347) and (2878) inclusive',average_votes)
       



