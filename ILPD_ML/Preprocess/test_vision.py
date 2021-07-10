import unittest
import vision as vs

class TestVision(unittest.TestCase):
    @classmethod
    def setUpClass(cls) :
        myvision = vs.Vision()
        file = myvision.load_file()

    def tearDown(self) -> None:
        pass

    def test_load_file(self):
        self.assertEqual(TestVision.file,1)

    def test_l2(self):

        result = 1
        self.assertEqual(result,1)

    def test_l3(self):

        result = 1
        self.assertEqual(result,1)

if __name__ == '__main__':
    unittest.main()