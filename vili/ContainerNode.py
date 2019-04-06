from io import TextIOWrapper

from PyVili.Node import Node
from PyVili.Types import NodeType


class ContainerNode(Node):
    def _init(self, parent: 'ContainerNode', id: str = ""):
        super()._init(parent, id)
        self.type = NodeType.ContainerNode

    def removeOwnership(self, element: Node):
        element.removeParent(self)
        return element

    def extractElement(self, element: Node):
        raise NotImplementedError(
            "ContainerNode::extractElement is abstract method")

    def copy(self, newParent: 'ContainerNode', newId: str = ""):
        raise NotImplementedError("ContainerNode::copy is abstract method")

    def write(self, writeFile: TextIOWrapper):
        raise NotImplementedError("ContainerNode::write is abstract method")
