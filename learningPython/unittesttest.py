import unittest

def addNum(a,b):
    return a+b
def delNum(a,b):
    return a-b

class TestFun(unittest.TestCase):
    def testAdd(self):
        self.assertEqual(2,addNum(1,1))
        
    def testDel(self):
        self.assertEqual(0,delNum(1,1))

if __name__=='__main__':
    unittest.main()
    
suite = unittest.TestLoader().loadTestsFromTestCase(TestFun)
#suite = unittest.TestSuite()
#suite.addTest(ParametrizedTestCase.parametrize(TestOne, param=42))
#suite.addTest(ParametrizedTestCase.parametrize(TestOne, param=13))
unittest.TextTestRunner(verbosity=2).run(suite)
