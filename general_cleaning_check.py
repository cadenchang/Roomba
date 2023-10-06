import bt_library as btl
from globals import GENERAL_CLEANING


class GeneralCheck(btl.Condition):
    
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Checking general cleaning command")
        if blackboard.get_in_environment(GENERAL_CLEANING, False) == True:
            return self.report_succeeded(blackboard)
        else:
            return self.report_failed(blackboard)
