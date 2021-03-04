import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    
    emp_1 = Employee('Corey','Anderson',50000)
    emp_2 = Employee('Scarlett','Johnson',60000)
    
    def test_fullname(self):
          
        emp_1 = Employee('Corey','Anderson',50000)
        emp_2 = Employee('Scarlett','Johnson',60000)
        
            
        self.assertEqual(emp_1.name(),'Corey Anderson')
        self.assertEqual(emp_2.name(),'Scarlett Johnson')
        
        emp_1.first_name = 'Brijraj'
        emp_2.first_name = 'Mahek'
        
        self.assertEqual(emp_1.name(),'Brijraj Anderson')
        self.assertEqual(emp_2.name(),'Mahek Johnson')
        
        
    def test_email(self):
        
        emp_1 = Employee('Corey','Anderson',50000)
        emp_2 = Employee('Scarlett','Johnson',60000)
        
        self.assertEqual(emp_1.email(),'Corey.Anderson@gmail.com')
        self.assertEqual(emp_2.email(),'Scarlett.Johnson@gmail.com')
        
        emp_1.first_name = 'Brijraj'
        emp_2.first_name = 'Mahek'
        
        self.assertEqual(emp_1.email(),'Brijraj.Anderson@gmail.com')
        self.assertEqual(emp_2.email(),'Mahek.Johnson@gmail.com')
        
        
if __name__ == '_main__':
    unittest.main()