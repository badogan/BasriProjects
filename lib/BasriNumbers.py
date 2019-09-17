class BasriNumbers:
    
    def __init__(self, num1,num2):
        self.num1 = num1
        self.num2 = num2
    
    def MultiplyThem(self):
        '''
        multiply them
        >>> BasriNumbers(10,20).MultiplyThem()
        200.0
        '''
        return float(self.num1*self.num2)
    
    def AddThem(self):
        '''
        add them
        >>> BasriNumbers(10,20).AddThem()
        30.0
        '''
        return float(self.num1+self.num2)

class ArdaNumbers(BasriNumbers):
    def __init__(self, num1, num2):
            super().__init__(num1, num2)
            self.num1 = 20*num1
            self.num2 = num2
            
    def DivideThem(self):
        ''' Divide is not straightforward!
        divide them - but the first number is multiplied with 20 first!
        >>> ArdaNumbers(10,20).DivideThem()
        10.0
        '''
        return float(self.num1/self.num2)
