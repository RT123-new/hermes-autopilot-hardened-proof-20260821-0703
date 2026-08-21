"""
Sequential dispatcher entity.
"""
class Dispatcher:
    def __init__(self):
        self.queue = []
        self.executed = []

    def enqueue(self, task_name: str):
        self.queue.append(task_name)

    def process_all(self):
        while self.queue:
            task = self.queue.pop(0)
            self.executed.append(task)
        return len(self.executed)
