import bt_library as btl

class UntilFails(btl.Decorator):
    def __init__(self, child: btl.TreeNode):
        super().__init__(child)
        
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        if self.child.run(blackboard) == btl.ResultEnum.FAILED:
            return self.report_succeeded(blackboard)
        else:
            return self.report_running(blackboard)