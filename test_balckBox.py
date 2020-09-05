import unittest

def sum_test_positive(num1, num2):
    return num1 + num2
    
def sum_test_negative(num1, num2):
    return num1 + num2
    

class black_box(unittest.TestCase):
    
    def test_sum_positive(self):
        num_1 = 10
        num_2 = 5

        answer = sum_test_positive(num_1, num_2)
        self.assertEqual(answer,15)

    def test_sum_negative(self):
        num_1 = -15
        num_2 = -10

        answer = sum_test_negative(num_1, num_2)
        self.assertEqual(answer, -25)



if __name__ == "__main__":
    unittest.main()

