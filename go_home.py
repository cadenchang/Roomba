import bt_library as btl
from globals import HOME_PATH


class GoHome(btl.Task):
    
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("going home")

        blackboard.set_in_environment(HOME_PATH, "")

        return self.report_succeeded(blackboard)
