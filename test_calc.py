import unittest
import calc


class TestCalc(unittest.TestCase):
    
    def test_add(self):
        
        self.assertEqual(calc.add(20,5),25)
        self.assertEqual(calc.add(-1,1),0)
        self.assertEqual(calc.add(-1,-1),-2)
        
    def test_mul(self):
        
        self.assertEqual(calc.mul(10,20),200)
        self.assertEqual(calc.mul(-10,20),-200)
        self.assertEqual(calc.mul(-10,-20),200)
    
    def test_subs(self):
        
        self.assertEqual(calc.subs(10,20),-10)
        self.assertEqual(calc.subs(-10,20),-30)
        self.assertEqual(calc.subs(-10,-20),10)
        
    def test_div(self):
        
        self.assertEqual(calc.div(10,20),0.5)
        self.assertEqual(calc.div(-10,20),-0.5)
        self.assertEqual(calc.div(-10,-20),0.5)
        self.assertEqual(calc.div(-10,-20),0.5)
        self.assertEqual(calc.div(10,0),0.5)
    
    
        


        
        
if __name__ == '__main__':
    unittest.main()