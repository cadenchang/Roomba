from typing import Dict, Any, Optional

from .common import EnvironmentKeyType, NodeIdType


class Blackboard:
    """
    Class of the blackboard.
    """
    __environment: Dict[EnvironmentKeyType, Any]  # State of the environmental variables
    __states: Dict[NodeIdType, Any]  # State of the nodes

    def __init__(self):
        self.__states = dict()
        self.__environment = dict()

    """
        Return the value in the environment associated with the specified key.
        :param key: Key to query
        :param default_value: Value to return if the node state was not found in the blackboard
        :return: The value associated with the key (if it exists)
    """
    def get_in_environment(self, key: EnvironmentKeyType, default_value: Optional[Any]) -> Any:  
        return self.__environment[key] if key in self.__environment else default_value

    """
        Return the value in the states associated with the specified node ID.
        :param node_id: Identification of the node to query
        :return: The value associated with the node ID (if it exists)
    """
    def get_in_states(self, node_id: NodeIdType) -> Any:
        return self.__states[node_id] if node_id in self.__states else None

    """
        Return TRUE if the specified node ID is in the states map.
        :param node_id: Identification of the node to query
        :return: TRUE if the node ID is in the states map
    """
    def is_in_states(self, node_id: NodeIdType) -> bool:
        return node_id in self.__states

    """
        Set a variable in the environment portion of the blackboard.
        :param key: Key to set
        :param value: Value associated with the key
    """
    def set_in_environment(self, key: EnvironmentKeyType, value: Any) -> None:
        self.__environment[key] = value

    """
        Set a variable in the states portion of the blackboard.
        :param node_id: Identification of the node to set
        :param value: Value associated with the key
    """
    def set_in_states(self, node_id: NodeIdType, value: Any) -> None:
        self.__states[node_id] = value
