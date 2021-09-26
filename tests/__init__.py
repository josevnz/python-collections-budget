import ast
from pathlib import Path
from os import path


def get_real_path(filename):
    parent_dir = Path(__file__).parent.parent
    return path.join(parent_dir, filename)


def load_ast_tree(filename):
    try:
        with open(get_real_path(filename)) as f:
            fstr = f.read()
            return ast.parse(fstr, filename=filename)
    except IOError:
        return ast.parse("()")
