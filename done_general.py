import bt_library as btl
from globals import GENERAL_CLEANING


class DoneGeneral(btl.Task):
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        blackboard.set_in_environment(GENERAL_CLEANING, False)
        return self.report_succeeded(blackboard)
