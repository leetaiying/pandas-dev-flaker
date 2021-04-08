import ast
from typing import Iterator, Tuple

from pandas_style_guide._ast_helpers import is_name_attr
from pandas_style_guide._data import State, register

MSG = "PSG006 do not use unitest.mock, use pytest's monkeypatch"


@register(ast.Name)
def visit_Name(
    state: State,
    node: ast.Name,
    parent: ast.AST,
) -> Iterator[Tuple[int, int, str]]:
    if is_name_attr(node, state.from_imports, "unittest", ("mock",)):
        yield node.lineno, node.col_offset, MSG


@register(ast.Attribute)
def visit_Attribute(
    state: State,
    node: ast.Attribute,
    parent: ast.AST,
) -> Iterator[Tuple[int, int, str]]:
    if (
        node.attr == "mock"
        and isinstance(node.value, ast.Name)
        and node.value.id == "unittest"
    ):
        yield node.lineno, node.col_offset, MSG
