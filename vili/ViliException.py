class ViliException(Exception):
    def __init__(self, msg, dct):
        self.msg = msg
        for word in dct:
            self.msg = self.msg.replace("%" + word + "%", str(dct[word]))
        super().__init__(self.msg)


class NodeAlreadyHaveParentException(ViliException):
    def __init__(self, dct):
        super().__init__("Node %path% already has a parent : %parent%", dct)


class NodeChangeIDWithParentException(ViliException):
    def __init__(self, dct):
        super().__init__("Can't change id of %path% when it has a parent : %parent%", dct)


class NodeWrongParentRemoverException(ViliException):
    def __init__(self, dct):
        super().__init__("%wrongparent% is not %path% parent", dct)


class NodeInvalidIdException(ViliException):
    def __init__(self, dct):
        super().__init__("Invalid Id for Node : '%id%'", dct)


class DataNodeInvalidDataTypeException(ViliException):
    def __init__(self, dct):
        super().__init__("Invalid DataType : '%type%' for DataNode : %path%", dct)


class NodeInvalidParentException(ViliException):
    def __init__(self, dct):
        super().__init__("Invalid Parent : '%parent%' for Node : %id%", dct)


class DataNodeWrongAutosetException(ViliException):
    def __init__(self, dct):
        super().__init__("Can't autoset raw value %data% for DataNode %path%", dct)


class DataNodeWrongDataTypeException(ViliException):
    def __init__(self, dct):
        super().__init__("DataType %datatype% is not valid for DataNode %path%", dct)


class ComplexNodeNoPathPartsError(ViliException):
    def __init__(self, dct):
        super().__init__("ComplexNode %path% <at> method call must have at least one path part", dct)


class ComplexNodeIncorrectChildTypeException(ViliException):
    def __init__(self, dct):
        super().__init__("Child '%child%' of ComplexNode '%path%' has type %type%", dct)


class ComplexNodeEmptyPathException(ViliException):
    def __init__(self, dct):
        super().__init__("ComplexNode '%path%' can't access empty path", dct)
