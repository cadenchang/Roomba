import bt_library as btl


class Sequence(btl.Composite):

    def __init__(self, children: btl.NodeListType):
        super().__init__(children)

    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        child_position = self.additional_information(blackboard, 0)

        while child_position < len(self.children):
            child = self.children[child_position]
            result_child = child.run(blackboard)
            if result_child == btl.ResultEnum.FAILED:
                return self.report_failed(blackboard, 0)
            
            if result_child == btl.ResultEnum.RUNNING:
                return self.report_running(blackboard, child_position)

            child_position = child_position + 1

        return self.report_succeeded(blackboard, 0)
