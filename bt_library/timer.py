from .blackboard import Blackboard
from .common import ResultEnum
from .decorator import Decorator
from .tree_node import TreeNode


class Timer(Decorator):
    TIMER_NOT_IN_USE = -1

    __time: int

    """
        Default constructor.
        :param time: Duration of the timer [counts]
        :param child: Child associated to the decorator
    """
    def __init__(self, time: int, child: TreeNode):
        super().__init__(child)
        self.__time = time

    """
        Execute the behavior of the node.
        :param blackboard: Blackboard with the current state of the problem
        :return: The result of the execution
    """
    def run(self, blackboard: Blackboard) -> ResultEnum:
        
        timer_period = self.additional_information(blackboard, Timer.TIMER_NOT_IN_USE)
        time_to_expiration = timer_period if timer_period > Timer.TIMER_NOT_IN_USE else self.__time

        time_to_expiration = time_to_expiration - 1

        if time_to_expiration < 0:
            return self.report_succeeded(blackboard, Timer.TIMER_NOT_IN_USE)

        self.print_message(f"time-to-expiration = {time_to_expiration}")
        result_child = self.child.run(blackboard)

        if result_child == ResultEnum.FAILED:
            return self.report_failed(blackboard, Timer.TIMER_NOT_IN_USE)

        return self.report_running(blackboard, time_to_expiration)
