from typing import Any, Optional

from .blackboard import Blackboard
from .common import NodeIdType, NODE_RESULT, ADDITIONAL_INFORMATION, ResultEnum

__identification_counter__: int = 0


class TreeNode:
    __id: NodeIdType  # Identification of the node

    def __init__(self):
        global __identification_counter__
        self.__id = __identification_counter__
        __identification_counter__ = __identification_counter__ + 1

    """
        Return the custom state associated with the node.
        :param blackboard: Blackboard with the current state of the tree
        :param default_value: Value to return if the node state was not found in the blackboard
        :return: State of this node or None if not found
    """
    def additional_information(self, blackboard: Blackboard, default_value: Optional[Any]) -> Any:
        
        result = default_value
        if blackboard.is_in_states(self.__id):
            state = blackboard.get_in_states(self.__id)
            if ADDITIONAL_INFORMATION in state:
                result = blackboard.get_in_states(self.__id)[ADDITIONAL_INFORMATION]
        return result

    """
        :return: Return the identification of the node
    """
    @property
    def id(self) -> NodeIdType:
        return self.__id

    """
        :return: Return the pretty version of the node class and identification
    """
    @property
    def pretty_id(self) -> str:
        return f"{self.__class__.__name__}({self.__id})"

    """
        Print the specified message with a pretty print.
        :param message: Message to print
    """
    def print_message(self, message: str):
        print(f"{self.pretty_id}: {message}")

    """
        Before returning a failed state, print it in a human-readable way.
        :param blackboard: Blackboard with the current state of the problem
        :param additional_information: Additional information for the node to store in the blackboard
        :return: The specified result
    """
    def report_failed(self, blackboard: Blackboard, additional_information: Any = None):
        
        blackboard.set_in_states(
            self.__id,
            {NODE_RESULT: ResultEnum.FAILED, ADDITIONAL_INFORMATION: additional_information}
        )
        self.print_message("FAILED")
        return ResultEnum.FAILED

    """
        Before returning a running state, print it in a human-readable way.
        :param blackboard: Blackboard with the current state of the problem
        :param additional_information: Additional information for the node to store in the blackboard
        :return: The specified result
    """
    def report_running(self, blackboard: Blackboard, additional_information: Any = None):
        
        blackboard.set_in_states(
            self.__id,
            {NODE_RESULT: ResultEnum.RUNNING, ADDITIONAL_INFORMATION: additional_information}
        )
        self.print_message("RUNNING")
        return ResultEnum.RUNNING

    """
        Before returning the succeeded state, print it in a human-readable way.
        :param blackboard: Blackboard with the current state of the problem
        :param additional_information: Additional information for the node to store in the blackboard
        :return: The specified result
    """
    def report_succeeded(self, blackboard: Blackboard, additional_information: Any = None):
        
        blackboard.set_in_states(
            self.__id,
            {NODE_RESULT: ResultEnum.SUCCEEDED, ADDITIONAL_INFORMATION: additional_information}
        )
        self.print_message("SUCCEEDED")
        return ResultEnum.SUCCEEDED

    """
        Find the result of the node in the specified blackboard.
        :param blackboard: Blackboard with the current state of the tree
        :return: Result of this node or None if not found
    """
    def result(self, blackboard: Blackboard) -> ResultEnum:
        if not blackboard.is_in_states(self.__id):
            return ResultEnum.UNDEFINED
        return blackboard.get_in_states(self.__id)[NODE_RESULT]

    """
        Execute the behavior of the node.
        :param blackboard: Blackboard with the current state of the problem
        :return: The result of the execution
    """
    def run(self, blackboard: Blackboard) -> ResultEnum:
        return self.report_failed(blackboard)
