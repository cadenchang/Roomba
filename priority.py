import bt_library as btl

class Priority(btl.Composite):

    def __init__(self, children: btl.NodeListType):
        super().__init__(children)


    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:

        for child in self.children:
            result_child = child.run(blackboard)
            if result_child == btl.ResultEnum.SUCCEEDED:
                return self.report_succeeded(blackboard, 0)

            if result_child == btl.ResultEnum.RUNNING:
                return self.report_running(blackboard, 0)


        return self.report_failed(blackboard, 0)


        