# API Stubs for VEXcode Python & Robot Mesh VEX Python B

[![codecov](https://codecov.io/gh/VEX-Robotics-AI/VEX-Py/branch/master/graph/badge.svg)](https://codecov.io/gh/VEX-Robotics-AI/VEX-Py/tree/master)

##  Robot Mesh VEX Python B

Modules not stubbed:
- `__bi` / `built_ins` (subset of Python's built-ins)
- `dict` (subset of Python's built-in `dict`; NOTE: NO `.items()`)
- `func` (not clear what it is for)
- `list` (subset of Python's built-in `list`)
- `margin` (not clear what it is for)
- `math` (subset of Python's built-in `math` module)
- `random` (subset of Python's built-in `random` module)
- `string` (subset of Python's built-in `string` module)
- `sys`: clash with Python's built-in `sys` module, with some extra funcs:
  - `run_in_thread`
  - `wait_for`


# Testing

Without coverage (fast):
```bash
  python3 -m pytest src/
```

With coverage:
```bash
  python3 -m pytest --cov src/
```
