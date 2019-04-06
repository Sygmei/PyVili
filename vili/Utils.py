def isStringInt(s: str):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


def isStringFloat(s: str):
    if len(s) > 0:
        s = s[1::] if s[0] == "-" else s
        if s.count(".") == 1 and s[0] != ".":
            if isStringInt(s.replace(".", "")):
                return True
    return False
