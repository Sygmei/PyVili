from io import TextIOWrapper

from PyVili.ViliException import (
    NodeAlreadyHaveParentException,
    NodeChangeIDWithParentException,
    NodeWrongParentRemoverException,
    NodeInvalidIdException,
    NodeInvalidParentException)

from PyVili.Types import NodeType


class Node:
    def _init(self, parent: 'ContainerNode', id: str = ""):
        from PyVili import ContainerNode
        if isinstance(parent, str) and id == "":
            self.id = parent
            self.parent = None
        else:
            self.parent = parent
            self.id = id
        self.type = NodeType.Node
        self.annotation = ""
        self.visible = True
        if not isinstance(self.id, str) or self.id == "":
            raise NodeInvalidIdException({"id": id})
        if self.parent is not None and not isinstance(self.parent, ContainerNode):
            raise NodeInvalidParentException({"parent": parent, "id": id})

    def removeParent(self, currentParent):
        if self.parent is None or self.parent == currentParent:
            self.parent = None
        else:
            raise NodeWrongParentRemoverException(
                {"wrongparent": currentParent.getNodePath(), "path": self.getNodePath()}
            )

    def setAnnotation(self, annotation: str):
        self.annotation = annotation

    def getAnnotation(self):
        return self.annotation

    def getId(self):
        return self.id

    def setId(self, id: str):
        if self.parent is None:
            self.id = id
        else:
            raise NodeChangeIDWithParentException(
                {"path": self.getNodePath(), "parent": self.parent.getNodePath()}
            )

    def getType(self):
        return self.type

    def setParent(self, parent: 'ContainerNode'):
        if self.parent is None:
            self.parent = parent
        else:
            raise NodeAlreadyHaveParentException(
                {"path": self.getNodePath(), "parent": self.parent.getNodePath()}
            )

    def getParent(self):
        return self.parent

    def getNodePath(self):
        parentChain = []
        currentParent = self.parent
        while currentParent is not None:
            parentAnnotation = "" if currentParent.getAnnotation() == "" else "<" + \
                currentParent.getAnnotation() + ">"
            parentChain.append(currentParent.getId() + parentAnnotation)
            currentParent = currentParent.getParent()
        parentChain = parentChain[::-1]
        parentChain.append(self.id + "" if self.annotation
                           == "" else "<" + self.annotation + ">")
        return "/".join(parentChain)

    def getRawNodePath(self):
        parentChain = []
        currentParent = self.parent
        while currentParent is not None:
            parentChain.append(currentParent.getId())
            currentParent = currentParent.getParent()
        parentChain = parentChain[::-1]
        parentChain.append(self.id)
        return "/".join(parentChain)

    def getDepth(self):
        currentParent = self.parent
        depth = 0
        while currentParent is not None:
            currentParent = currentParent.getParent()
            depth += 1
        return depth

    def getVisible(self):
        return self.visible

    def setVisible(self, visible: bool):
        self.visible = visible

    def copy(self, newParent: 'ContainerNode', newId: str = ""):
        raise NotImplementedError("Node::copy is abstract method")

    def write(self, writeFile: TextIOWrapper):
        raise NotImplementedError("Node::write is abstract method")
