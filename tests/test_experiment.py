import unittest
from src.domain.experiment import Experiment

class TestExperiment(unittest.TestCase):
    def test_init(self):
        exp = Experiment("E1", "Test")
        self.assertEqual(exp.run(), "RUNNING")

if __name__ == "__main__":
    unittest.main()
