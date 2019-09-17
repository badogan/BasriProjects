#HelloWorldRoute
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
        return str(float(self.num1*self.num2))
