"""
Experiment domain entity with planted defect for falsification review testing.
"""
# SEEDED_DEFECT
class Experiment:
    def __init__(self, exp_id: str, name: str):
        self.exp_id = exp_id
        self.name = name
        self.status = "CREATED"

    def run(self):
        # PLANTED_BUG: Pre-check without concurrency lock
        self.status = "RUNNING"
        return self.status
