import bt_library as btl
from globals import HOME_PATH


class FindHome(btl.Task):
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Looking for a home")
        blackboard.set_in_environment(HOME_PATH, "Up Left Left Up Right")
        return self.report_succeeded(blackboard)
