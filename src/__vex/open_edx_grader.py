"""State-Sequence Grader."""


from gradelib import Grader, Test


class StateSeqGrader(Grader):
    """State-Sequence Grader."""

    def __init__(self, test_fn: callable, /):
        """Initialize State-Sequence Grader."""
        super().__init__()

        self.add_preprocessor(fn=test_fn)

        self.add_test(Test(test_fn=print,
                           short_description=test_fn.__doc__,
                           detailed_description=test_fn.__doc__,
                           compare=lambda _, actual: actual.endswith('True')))
