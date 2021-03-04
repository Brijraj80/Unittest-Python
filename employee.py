class Employee:
    inc = 1.05
    def __init__(self,first_name,last_name,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary 
        
    def name(self):
        return '{} {}'.format(self.first_name,self.last_name)
    
    def email(self):
        return '{}.{}@gmail.com'.format(self.first_name,self.last_name)
    
    def sal(self):
        self.salary = int(self.salary*self.inc)
        return '{}'.format(self.salary)
