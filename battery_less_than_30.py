import bt_library as btl
from globals import BATTERY_LEVEL


class BatteryLessThan30(btl.Condition):
    """
    Implementation of the condition "battery_level < 30".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Checking battery < 30")

        return self.report_succeeded(blackboard) \
            if blackboard.get_in_environment(BATTERY_LEVEL, 0) < 30 \
            else self.report_failed(blackboard)
