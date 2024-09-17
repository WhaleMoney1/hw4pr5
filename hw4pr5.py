# CSCI 1550: HW 4, Problem 5
# Filename: hw4pr5.py
# Name: 
#
# Task(s): Creating the int8 class!

from math import*


class int8: 
   num = 0
   king = 1
   derp = 2
   obj1 = 2
   obj2 = 298
   obj3 = 1
   
   def __add__(self, obj):   # self refers to the object that calls the method
       """ this overloads the __add__ method so that Python
           knows how to apply it to int8-objects
       """
       objOut = int8() # creating the int8 object that will be returned
       objOut.num = self.num + obj.num # updating the data-member, num
       return objOut
   
   def mystery(val): # this isn't a method that is pre-existing in Python
            """ A quick example of a static method """
            objOut = int8()
            objOut.num = val
            return objOut
   
   def int2int8(self):
       '''
       cuts off at 8 bits and leaves the crumbs
       '''
       return self & 255
   
   def setVal(self,val):
        '''
        '''
        self.num = int8.int2int8(val)
        return  

        
   
   
