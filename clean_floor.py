import bt_library as btl
import random

class CleanFloor(btl.Task):
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        rand = random.randint(0,9)
        if rand == 0:
            return self.report_failed(blackboard)
        else:
            return self.report_succeeded(blackboard)
        
