from .tree_node import TreeNode

class Decorator(TreeNode):
    
    __child: TreeNode  # Child associated with this decorator

    """
        Default constructor.
        :param child: Child for this node
    """
    def __init__(self, child: TreeNode):
        super().__init__()
        self.__child = child

    """
        Default constructor.
        :param child: Child for this node
    """
    @property
    def child(self) -> TreeNode:
        return self.__child
