import ast
from pandas_style_guide._data import register
from pandas_style_guide._ast_helpers import is_name_attr

MSG = 'PSG003 Do not use pytest.raises without context manager'
@register(ast.Call)
def check_contextless_pytest_raises(state, node, parent):
    if is_name_attr(node.func, state.from_imports, 'pytest', ('raises', )) and not isinstance(parent, ast.withitem):
        yield node.lineno, node.col_offset, MSG
    elif node.func.value.id == 'pytest' and node.func.attr == 'raises' and not isinstance(parent, ast.withitem):
        yield node.lineno, node.col_offset, MSG
