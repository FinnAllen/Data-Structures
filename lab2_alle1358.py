#Author Finnian Allen
#Date Assigned 9/17/19

class Zillion:
    def __init__(self, digits):
        self.myList = list()
        for i in digits:
            if i.isdigit():
                self.myList.append(i)
        if len(self.myList) == 0:
            raise RuntimeError

    def increment(self):
        length = len(self.myList)
        i = len(self.myList) - 1
        if self.myList[i] == '9':
            # the 9 loop
            while self.myList[i] == '9':
                if i == 0:
                    self.myList[0] = '1'#str(int(self.myList[0]))
                    self.myList.insert(1, '0')
                elif self.myList[i - 1]  == '9':
                    self.myList[i] = '0'
                elif i != 0 and self.myList[i - 1] != '9':
                    self.myList[i] = '0'
                    self.myList[i - 1] = str(int(self.myList[i - 1]) + 1)
                    break
                i -= 1
                    
                    
        else:
            self.myList[i] = str(int(self.myList[i]) + 1)

    def toString(self):
        newString = ''
        for i in self.myList:
            newString = newString + str(i)
        return newString

    def isZero(self):
        newInt = 0
        for i in self.myList:
            newInt = newInt + int(i)
        return newInt == 0
            
try:
    z = Zillion('')
except RuntimeError:
    print('Empty string')
# It must print 'Empty string' without apostrophes. 2 points.

try:
    z = Zillion(' , ')
except RuntimeError:
    print('No digits in the string')
# It must print 'No digits in the string' without apostrophes. 2 points.

try:
    z = Zillion(' + ')
except RuntimeError:
    print('Non-digit in the string')
# It must print 'Non-digit in the string' without apostrophes. 2 points.

try:
    z = Zillion('0')
except RuntimeError:
    print('This must not be printed')
#  It must print nothing. 2 points.

print(z.isZero())    #  It must print True. 2 points.

try:
    z = Zillion('000000000')
except RuntimeError:
    print('This must not be printed')
#  It must print nothing. 2 points.

print(z.isZero())    #  It must print True. 2 points.

try:
    z = Zillion('000 000 000')
except RuntimeError:
    print('This must not be printed')
#  It must print nothing. 2 points.

print(z.isZero())    #  It must print True. 2 points.

try:
    z = Zillion('997')
except RuntimeError:
    print('This must not be printed')
#  It must print nothing. 2 points.

print(z.isZero())    #  It must print False. 2 points.

print(z.toString())  #  It must print 997. 2 points.

z.increment()

print(z.toString())  #  It must print 998. 2 points.

z.increment()

print(z.toString())  #  It must print 999. 2 points.

z.increment()

print(z.toString())  #  It must print 1000. 2 points.

try:
    z = Zillion('0 9,9 9')
except:
    print('This must not be printed') #  It must print nothing.  3 points.

z.increment()

print(z.toString())  #  It must print 1000. 2 points.





