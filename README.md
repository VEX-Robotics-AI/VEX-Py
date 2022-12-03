# Python API Stubs for VEXcode & Robot Mesh Studio

[![codecov](https://codecov.io/gh/VEX-Robotics-AI/VEX-Py/branch/main/graph/badge.svg)](https://codecov.io/gh/VEX-Robotics-AI/VEX-Py)


## VEXcode

References:
- [VEXcode IQ Python](https://codeiq.vex.com)
- [VEXcode V5 Python](https://codev5.vex.com)


##  Robot Mesh Studio

References:
- [Robot Mesh VEX IQ Python B](https://www.robotmesh.com/studio/content/docs/vexiq-python_b//html/index.html)
- [Robot Mesh VEX V5 Python](https://www.robotmesh.com/studio/content/docs/vexv5-python//html/index.html)

Modules not stubbed:
- `__bi` / `built_ins` (subset of Python's built-ins)
- `dict` (subset of Python's built-in `dict`; NOTE: NO `.items()`)
- `func` (not clear what it is for)
- `list` (subset of Python's built-in `list`)
- `margin` (not clear what it is for)
- `math` (subset of Python's built-in `math` module)
- `random` (subset of Python's built-in `random` module)
- `string` (subset of Python's built-in `string` module)
- `sys` (clash with Python's built-in `sys` module)


# Contributing

We welcome PRs from VEX Robotics enthusiasts who like coding in Python using this stub library
in your favourite IDEs/editors.


# Testing

Without coverage (fast):
```bash
  python3 -m pytest src/
```

With coverage:
```bash
  python3 -m pytest --cov src/
```
