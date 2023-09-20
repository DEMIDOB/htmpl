class HTMPLOperation:
    TAG_NAME = ""

    def __init__(self, *, ctx: dict):
        self.ctx = ctx

    def perform(self, *args, **kwargs):
        for arg in args:
            return arg

        return "^_^"


class HTMPLOperationDocument(HTMPLOperation):
    TAG_NAME = "[document]"


class HTMPLOperationAdd(HTMPLOperation):
    TAG_NAME = "add"

    def perform(self, *args):
        res = 0

        for arg in args:
            try:
                res += int(arg)
            except ValueError:
                continue

        return res


class HTMPLOperationMul(HTMPLOperation):
    TAG_NAME = "mul"

    def perform(self, *args):
        res = 1

        for arg in args:
            try:
                res *= int(arg)
            except ValueError:
                continue

        return res


class HTMPLOperationInt(HTMPLOperation):
    TAG_NAME = "int"

    def perform(self, *args):
        res = 0

        for arg in args:
            res = int(arg)

        return res


class HTMPLOperationStr(HTMPLOperation):
    TAG_NAME = "str"

    def perform(self, *args):
        res = " ".join(list(map(str, args)))
        return res


class HTMPLOperationVar(HTMPLOperation):
    TAG_NAME = "var"

    def perform(self, *args, **kwargs):
        res = None
        val = None

        if kwargs:
            name = None
            for k in kwargs:
                name = k
                if name in self.ctx:
                    val = self.ctx[name]
                break

            for arg in args:
                # print("sdf", arg)
                val = arg
                break

            if name:
                self.ctx[name] = val
                # print(name, "=", val)
                res = val

        return res


class HTMPLOperationOut(HTMPLOperation):
    TAG_NAME = "out"

    def perform(self, *args):
        res = " ".join(list(map(str, args)))
        print(res)
        return res
