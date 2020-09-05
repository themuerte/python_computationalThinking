import unittest

def adult(age):
    if age >= 18:
        return True
    else:
        return False


class test_glass(unittest.TestCase):
    def test_old(self):
        age = 20
        answer = adult(age)

        self.assertEqual(answer, True)

    def test_young(self):
        age = 15
        answer = adult(age)
 
        self.assertEqual(answer, False)


if __name__ == "__main__":
    unittest.main()
