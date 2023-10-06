from typing import List

from .tree_node import TreeNode

NodeListType = List[TreeNode]  # Type definition for a list of tree nodes


class Composite(TreeNode):
    __children: NodeListType  # List of children of the composite

    """
        Default constructor
        :param children: List of children for this node
    """
    def __init__(self, children: NodeListType):
        super().__init__()
        self.__children = children

    """
        :return: Return the list of children in the composite
    """
    @property
    def children(self) -> NodeListType:
        return self.__children
