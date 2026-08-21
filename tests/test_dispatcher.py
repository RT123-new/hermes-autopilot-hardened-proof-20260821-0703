import unittest
from src.domain.dispatcher import Dispatcher

class TestDispatcher(unittest.TestCase):
    def test_dispatch(self):
        d = Dispatcher()
        d.enqueue("task_1")
        d.enqueue("task_2")
        self.assertEqual(d.process_all(), 2)

if __name__ == "__main__":
    unittest.main()
