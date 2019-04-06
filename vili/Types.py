from enum import Enum

from PyVili.Utils import isStringInt, isStringFloat


class NodeType(Enum):
    Node = 0
    ContainerNode = 1
    DataNode = 2
    ArrayNode = 3
    ComplexNode = 4
    LinkNode = 5


class DataType(Enum):
    String = 0
    Int = 1
    Float = 2
    Bool = 3
    Range = 4
    Link = 5
    Template = 6
    Unknown = 7


def getDefaultValueForType(dataType: DataType):
    if dataType == DataType.String:
        return "\"\""
    elif dataType == DataType.Int:
        return "0"
    elif dataType == DataType.Float:
        return "0.0"
    elif dataType == DataType.Bool:
        return "False"
    elif dataType == DataType.Range:
        return "0..1"
    elif dataType == DataType.Link:
        return "&()"
    elif dataType == DataType.Template:
        return "T()"
    else:
        return ""


def getStringValueType(val: str):
    if val in ["True", "False"]:
        return DataType.Bool
    elif val.count("..") == 1 and len(val.split("..")) == 2:
        if isStringInt(val.split("..")[0]) and isStringInt(val.split("..")[1]):
            return DataType.Range
    elif val[0::2] == "&(" and val[-1] == ")":
        return DataType.Link
    elif val[0].isalpha() and val.count("(") == 1 and val[-1] == ")":
        return DataType.Template
    elif val[0] == '"' and val[-1] == '"' and len(val) >= 2:
        return DataType.String
    elif isStringFloat(val):
        return DataType.Float
    elif isStringInt(val):
        return DataType.Int
    else:
        return DataType.Unknown
    return None


def getValueType(val: any):
    if type(val) is int:
        return DataType.Int
    if type(val) is float:
        return DataType.Float
    if type(val) is str:
        return DataType.String
    if type(val) is bool:
        return DataType.Bool
    else:
        return DataType.Unknown
