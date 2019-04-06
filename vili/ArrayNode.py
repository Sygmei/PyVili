from io import TextIOWrapper

from PyVili.ContainerNode import ContainerNode
from PyVili.DataNode import DataNode
from PyVili.Node import Node
from PyVili.Types import getValueType, NodeType


class ArrayNode(ContainerNode):
    def __init__(self, parent: ContainerNode, id: str = ""):
        super()._init(parent, id)
        self.children = []
        self.iterIndex = 0
        self.type = NodeType.ArrayNode

    def reorder(self, index: int):
        for i in range(index, len(self.children)):
            self.removeOwnership(self.children[i])
            self.children[i].setId("#" + str(i))
            self.children[i].setParent(self)

    def size(self):
        return len(self.children)

    def get(self, index: int):
        return self.children[index]

    def __getitem__(self, index: int):
        return self.children[index]

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterIndex >= self.size():
            self.iterIndex = 0
            raise StopIteration
        else:
            self.iterIndex += 1
            return self.children[self.iterIndex - 1]

    def push(self, value: any):
        newNode = DataNode(
            self, "#" + str(len(self.children)), getValueType(value))
        newNode.set(value)
        self.children.append(newNode)

    def insert(self, index: int, value: any):
        newNode = DataNode(self, "#" + str(index), getValueType(value))
        newNode.set(value)
        self.children.insert(0, newNode)

    def clear(self):
        self.children.clear()

    def erase(self, index: int):
        self.children.remove(index)

    def extractElement(self, element: Node):
        for index, elem in enumerate(self.children):
            if elem is element:
                self.removeOwnership(elem)
                self.erase(index)

    def copy(self, newParent: ContainerNode, newId: str = ""):
        pass

    def write(self, writeFile: TextIOWrapper):
        from PyVili import ViliParser
        if self.visible:
            for i in range(self.getDepth()):
                writeFile.write(ViliParser.spacing * " ")
            writeFile.write(self.id + ":[\n")
            for child in self.children:
                child.write(writeFile)
            for i in range(self.getDepth()):
                writeFile.write(ViliParser.spacing * " ")
            writeFile.write("]\n")
