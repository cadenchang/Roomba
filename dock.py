import bt_library as btl
from globals import BATTERY_LEVEL


class Dock(btl.Task):
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        
        return self.report_succeeded(blackboard)
