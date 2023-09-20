import sys

import bs4

import operations


def parse(*, ctx: dict = None, src: str = None, root: bs4.PageElement = None, rd=0):
    if not (src or root):
        raise "None of the arguments (src or root) is passed to the parse function!"

    if ctx is None:
        ctx = dict()

    if src:
        src = src.replace("\n", "").replace("&lt;", "<").replace("&gt;", ">")
        root = bs4.BeautifulSoup(src, features="html.parser")

    try:
        args = []
        for child in root.children:
            child_name = child.name
            if type(child_name) is str:
                args.append(parse(ctx=ctx, root=child, rd=rd + 1))
            else:
                for str_arg in child.text.split():
                    if not str_arg:
                        continue
                    args.append(str_arg)

        for operation in operations.OPERATIONS:
            if root.name == operation.TAG_NAME:
                return operation(ctx=ctx).perform(*args, **root.attrs)
    except AttributeError:
        print(root)

    return None


def main():
    filename = ""
    quit = False

    for arg in sys.argv:
        filename = arg
        if filename == "main.py":
            quit = True
            continue

        if quit:
            break

    with open(filename, "r") as file:
        ctx = dict()
        res = parse(ctx=ctx, src=file.read())

if __name__ == '__main__':
    main()
