import ast
import math
import operator
import sys

BIN_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}
UNARY_OPS = {ast.UAdd: operator.pos, ast.USub: operator.neg}

FUNCTIONS = {
    "sqrt": math.sqrt, "abs": abs, "round": round,
    "sin": math.sin, "cos": math.cos, "tan": math.tan,
    "asin": math.asin, "acos": math.acos, "atan": math.atan,
    "log": math.log, "log10": math.log10, "log2": math.log2, "exp": math.exp,
    "floor": math.floor, "ceil": math.ceil, "factorial": math.factorial,
    "deg": math.degrees, "rad": math.radians,
}
CONSTANTS = {"pi": math.pi, "e": math.e}


def evaluate(expr: str, variables: dict | None = None) -> float:
    names = {**CONSTANTS, **(variables or {})}
    tree = ast.parse(expr.replace("^", "**"), mode="eval")

    def ev(node):
        if isinstance(node, ast.Expression):
            return ev(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value
        if isinstance(node, ast.BinOp) and type(node.op) in BIN_OPS:
            left, right = ev(node.left), ev(node.right)
            if isinstance(node.op, ast.Pow) and abs(right) > 10_000:
                raise ValueError("слишком большая степень")
            return BIN_OPS[type(node.op)](left, right)
        if isinstance(node, ast.UnaryOp) and type(node.op) in UNARY_OPS:
            return UNARY_OPS[type(node.op)](ev(node.operand))
        if isinstance(node, ast.Name):
            if node.id in names:
                return names[node.id]
            raise NameError(f"неизвестное имя: {node.id}")
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and not node.keywords:
            func = FUNCTIONS.get(node.func.id)
            if func is None:
                raise NameError(f"неизвестная функция: {node.func.id}")
            return func(*(ev(arg) for arg in node.args))
        raise SyntaxError("недопустимое выражение")

    return ev(tree)


def format_number(x) -> str:
    if isinstance(x, float) and x.is_integer() and abs(x) < 1e16:
        return str(int(x))
    return repr(round(x, 12)) if isinstance(x, float) else str(x)


def repl() -> None:
    print("Калькулятор. Пример: 2*(3+4)^2, sqrt(2), sin(pi/2), ans*10. Выход: q")
    ans = 0
    while True:
        try:
            line = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if line.lower() in {"q", "quit", "exit", "выход"}:
            break
        if not line:
            continue
        try:
            ans = evaluate(line, {"ans": ans})
            print("=", format_number(ans))
        except ZeroDivisionError:
            print("Ошибка: деление на ноль")
        except Exception as exc:
            print(f"Ошибка: {exc}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(format_number(evaluate(" ".join(sys.argv[1:]))))
    else:
        repl()
