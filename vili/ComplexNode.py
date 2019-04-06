from collections import OrderedDict
from io import TextIOWrapper

from PyVili.ArrayNode import ArrayNode
from PyVili.ContainerNode import ContainerNode
from PyVili.DataNode import DataNode
from PyVili.Node import Node
from PyVili.Types import NodeType
from PyVili.ViliException import (
    ComplexNodeNoPathPartsError,
    ComplexNodeIncorrectChildTypeException,
    ComplexNodeEmptyPathException)


def convertPath(path: str) -> list:
    if "." in path:
        rpath = list(filter(lambda a: a != "", path.split(".")))
        return rpath
    elif path != "":
        return [path]
    else:
        return []


class ComplexNode(ContainerNode):
    def __init__(self, parent: ContainerNode, id: str = ""):
        super()._init(parent, id)
        self.children = OrderedDict()
        self.type = NodeType.ComplexNode

    def extractElement(self, element: Node) -> Node:
        for index, elem in enumerate(self.children):
            if elem is element:
                self.removeOwnership(elem)
                self.children.pop(elem.getId())
                return elem

    def __getitem__(self, key: str) -> Node:
        return self.children[key]

    def get(self, key: str) -> Node:
        return self.children[key]

    def getDataNode(self, key: str) -> DataNode:
        if self.get(key).getType() == NodeType.DataNode:
            return self.children[key]
        raise ComplexNodeIncorrectChildTypeException({"path": self.getNodePath(),
                                                      "type": self.get(key).getType(), "child": key})

    def getComplexNode(self, key: str) -> 'ComplexNode':
        if self.get(key).getType() == NodeType.ComplexNode:
            return self.children[key]
        raise ComplexNodeIncorrectChildTypeException({"path": self.getNodePath(),
                                                      "type": self.get(key).getType(), "child": key})

    def getArrayNode(self, key: str) -> 'ArrayNode':
        if self.get(key).getType() == NodeType.ArrayNode:
            return self.children[key]
        raise ComplexNodeIncorrectChildTypeException({"path": self.getNodePath(),
                                                      "type": self.get(key).getType(), "child": key})

    def at(self, *pathParts: str):
        if len(pathParts) >= 2:
            return self.get(pathParts[0]).at(*pathParts[1::])
        elif len(pathParts) == 1:
            return self.get(pathParts[0])
        else:
            raise ComplexNodeNoPathPartsError({"path": self.getNodePath()})

    def getPath(self, path: str) -> Node:
        sPath = convertPath(path)
        if len(sPath) > 0:
            pathIndex = 0
            getToPath = self.getComplexNode(sPath[0])
            while pathIndex != len(sPath):
                getToPath = getToPath.getComplexNode(sPath[pathIndex])
                pathIndex += 1
            return getToPath
        raise ComplexNodeEmptyPathException({"path": self.getNodePath()})

    def getAll(self, nodeType: NodeType = NodeType.Node):
        elems = []
        for elem in self.children.values():
            if elem.getType() == nodeType or nodeType == NodeType.Node:
                elems.append(elem)
            elif elem.getType in [NodeType.ComplexNode, NodeType.ArrayNode] and nodeType == NodeType.ContainerNode:
                elems.append(elem)
        return elems

    def __contains__(self, item: str):
        if item in self.children:
            return True
        return False

    def contains(self, nodeType: NodeType, key: str):
        if key in self.children and self.children[key].getType() == nodeType:
            return True
        return False

    def push(self, node: Node):
        self.children[node.getId()] = node
        node.setParent(self)
        return node

    def write(self, writeFile: TextIOWrapper):
        from PyVili import ViliParser
        if self.visible:
            for i in range(self.getDepth()):
                writeFile.write(ViliParser.spacing * " ")
            writeFile.write(self.id + ":\n")
            for child in self.children:
                self.children[child].write(writeFile)
            writeFile.write("\n")

    def copy(self, newParent: ContainerNode, newId: str = ""):
        pass
