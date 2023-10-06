import bt_library as btl
from globals import SPOT_CLEANING

class SpotCheck(btl.Condition):
    
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Checking spot cleaning command")

        if blackboard.get_in_environment(SPOT_CLEANING, False) == True:
            return self.report_succeeded(blackboard)
        else:
            return self.report_failed(blackboard)
