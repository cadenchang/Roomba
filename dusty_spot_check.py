import bt_library as btl
from globals import DUSTY_SPOT_SENSOR


class DustySpotCheck(btl.Condition):
    
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        if blackboard.get_in_environment(DUSTY_SPOT_SENSOR, False) == True:
            self.print_message("Dusty Spot Found!")
            return self.report_succeeded(blackboard)
        else:
            return self.report_failed(blackboard)
