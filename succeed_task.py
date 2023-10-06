import bt_library as btl

class SucceedTask(btl.Task):
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        return self.report_succeeded(blackboard)
