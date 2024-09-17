# CSCI 1550: HW 4, Problem 5
# Filename: hw4pr5.py
# Name: Eion
#
# Task(s): Creating the int8 class!

class int8:
    num = 0

    
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
       ''' int2int8 takes a int8 object and truncates its binary values to be at most 8 bits long (or under 255)
       returns int8 object
       '''
       return self & 255
    
    def setVal(self,val):
       ''' setVal takes 2 arguments, self an int8 object and val an int
           and sets val to be the integer value for self
           returns nothing, ony sets a type
       '''
       self.num = int8.int2int8(val)
       return 
    
    def getVal(self):
       ''' getVal allows the user to extract the integer value from an int8 object
           returns an integer
       '''
       return self.num
    
    def __add__(self,obj):
       ''' __add__() overwrites the + operator and allows them to interact with int8 objects by adding their integer values held by the int8 objects
       returns: an int8 object
       '''
       out = int8()
       out.setVal(int8.int2int8(self.num+obj.num))
       return out

    def __neg__(self):
       '''__neg__() overwrites the - operator and allows them to interact with int8 objects by negating self
       returns an int8 object
       '''
       bits = int8.int2int8(self.num)
       flipped = ~bits
       Plusone = flipped.__add__(1)  
       out = int8()
       out.setVal(int8.int2int8(Plusone))
       return out
    
    def __sub__(self,obj):
       '''__sub__() overwrites the - operator and allows them to interact with int8 objects by way of integer subtraction(using addition) of the integer values held by the int8 objects
       returns: an int8 object
       '''
       out = int8()
       out.setVal(int8.int2int8(obj.num.__neg__().__add__(self.num))) #code big ugly
       return out
    
    ##### TASK 2:


    def __repr__(self):
       ''' __repr__ displays the integer value of an int8 object in the form of a string
       returns a string
       '''
       return str(self.num)
    
    def divBy2(self):
      ''' divBy2 accepts an integer Self and returns that value divided by 2 using fast operations
      returns an integer
      '''
      return self >> 1
      
    
    def mod2(self):
       ''' mod2 accepts an integer self and returns the value of self%2 using fast operations and int8 methods
       returns an integer
       '''
       return self.__sub__(int8.divBy2(self)<< 1)
       

    def bit2string(self):
      ''' returns the string representation of an int8 object
      '''
      return str(self)
      
   
    def int8ToString(self):
       ''' int8ToString() accepts an int8 object and returns the string representation of the 8-bit binary representation of its integer value that it holds #say that ten times fast
       returns a string
       '''
       acc = ''  
       for b in range(8):
          modby2 = int8.mod2(self.num)
          self.num = int8.divBy2(self.num)
          acc = int8.bit2string(modby2) + acc
       return acc
