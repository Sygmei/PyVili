from io import TextIOWrapper

from PyVili.ContainerNode import ContainerNode
from PyVili.Node import Node
from PyVili.Types import NodeType, DataType, getDefaultValueForType, getStringValueType, getValueType
from PyVili.ViliException import (
    DataNodeInvalidDataTypeException,
    DataNodeWrongAutosetException,
    DataNodeWrongDataTypeException)


class DataNode(Node):
    def __init__(self, parent=None, id=None, dataType=None):
        if dataType is None:
            dataType = id
            id = parent
            parent = None
        super()._init(parent, id)
        if dataType is None or not isinstance(dataType, DataType):
            validType = False
            for vtype in [str, float, int, bool]:
                if type(dataType) is vtype:
                    self.data = dataType
                    self.dataType = getValueType(self.data)
                    validType = True
                    break
            if not validType:
                raise DataNodeInvalidDataTypeException(
                    {"path": self.getNodePath(), "type": dataType})
        else:
            self.dataType = dataType
            self.data = None
            self.autoset(getDefaultValueForType(self.dataType))
        self.type = NodeType.DataNode

    def checkType(self):
        if isinstance(self.data, str) and self.dataType == DataType.String:
            return True
        if (isinstance(self.data, int) or isinstance(self.data, float)) and (
                self.dataType == DataType.Int or self.dataType == DataType.Float):
            return True
        if isinstance(self.data, bool) and self.dataType == DataType.Bool:
            return True
        return False

    def set(self, data: any):
        self.data = data
        self.checkType()

    def autoset(self, data: str):
        if getStringValueType(data) == self.dataType:
            if self.dataType == DataType.Int:
                self.data = int(data)
            elif self.dataType == DataType.Float:
                self.data = float(data)
            elif self.dataType == DataType.String:
                self.data = data[1:-1]
                print("AFFECT = =================> ", data)
            elif self.dataType == DataType.Bool:
                self.data = True if data == "True" else False
            else:
                raise DataNodeWrongAutosetException(
                    {"path": self.getNodePath(), "data": data})
            self.checkType()
        else:
            raise DataNodeWrongAutosetException(
                {"path": self.getNodePath(), "data": data})

    def dumpData(self):
        print(self.id, self.data, self.dataType)
        if self.dataType == DataType.String:
            return "\"" + self.data + "\""
        elif self.dataType in [DataType.Int, DataType.Float]:
            return str(self.data)
        elif self.dataType == DataType.Bool:
            return "True" if self.data else "False"
        else:
            raise DataNodeWrongDataTypeException(
                {"path": self.getNodePath(), "datatype": self.dataType})

    def getDataType(self):
        return self.dataType

    def copy(self, newParent: ContainerNode, newId: str = ""):
        pass

    def write(self, writeFile: TextIOWrapper):
        from PyVili import ViliParser
        if self.visible:
            for i in range(self.getDepth()):
                writeFile.write(ViliParser.spacing * " ")
            writeFile.write((self.id + ":" + self.dumpData())
                            if self.id[0] != "#" else self.dumpData())
            writeFile.write("\n")
