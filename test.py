import unittest
from recognize_license_plate import recognize_license_plate
class TestRecognition(unittest.TestCase):
    def test_recognize_license_plate(self):
        
        result1 = recognize_license_plate("testPlates\plate1.jpg")
        self.assertEqual(result1,"B58BPS")
       
        result2=recognize_license_plate("testPlates\plate2.jpg")
        self.assertEqual(result2,"HD99LUX")

        result3=recognize_license_plate("testPlates\plate3.jpeg")
        self.assertEqual(result3,"CJ19DAK")

        result4=recognize_license_plate("testPlates\plate4.jpg")
        self.assertEqual(result4,"SN66XMZ")
        
        result5=recognize_license_plate("testPlates\plate5.jpg")
        self.assertEqual(result5,"HAMBISA")

    
if __name__ == '__main__':
    unittest.main()

