"""Documentation Decorators."""


from collections.abc import Sequence
from typing import Any, LiteralString


__all__: Sequence[str] = 'add_doc', 'robotmesh_doc', 'vexcode_doc'


# pylint: disable=too-few-public-methods


class add_doc:   # noqa: N801
    """Add documentation."""

    def __init__(self, doc_str: LiteralString = '', /):
        """Initialize decorator with docstring."""
        self.doc_str: LiteralString = doc_str

    def __call__(self, member: Any, /):
        """Add documentation."""
        member.__doc__ += self.doc_str
        return member


class robotmesh_doc(add_doc):   # noqa: N801
    """Add Robot Mesh Studio documentation."""

    def __init__(self, doc_str: LiteralString = '', /):
        """Initialize decorator with docstring."""
        super().__init__(f'\n\nROBOT MESH STUDIO:\n{doc_str}\n')


class vexcode_doc(add_doc):   # noqa: N801
    """Add VEXcode documentation."""

    def __init__(self, doc_str: LiteralString = '', /):
        """Initialize decorator with docstring."""
        super().__init__(f'\n\nVEXCODE:\n{doc_str}\n')
