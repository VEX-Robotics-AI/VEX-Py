"""State-Sequence Grader."""


from collections.abc import Callable
from inspect import stack
import os
from pathlib import Path
from pprint import pprint
from typing import Union

from grader_support.gradelib import Grader, Test
from grader_support.graderutil import change_directory
from grader_support.run import run

from xqueue_watcher.jailedgrader import main


OUTPUT_COMP_FUNC_TYPE: type = Callable[[Union[str, Path]], bool]


class StateSeqGrader(Grader):
    """State-Sequence Grader."""

    _SUBMISSION_MODULE_NAME: str = '_submission'
    _SUBMISSION_MODULE_FILE_NAME: str = f'{_SUBMISSION_MODULE_NAME}.py'

    def __init__(self, output_comp_func: OUTPUT_COMP_FUNC_TYPE, /):
        """Initialize State-Sequence Grader."""
        super().__init__()

        self.output_comp_func: OUTPUT_COMP_FUNC_TYPE = output_comp_func

        self.add_preprocessor(fn=lambda student_submission_str: '')

        self.add_test(Test(test_fn=print,
                           short_description=output_comp_func.__doc__,
                           detailed_description=output_comp_func.__doc__,
                           compare=lambda _, actual: actual.endswith('True')))

    def __call__(self,
                 student_submission_file_path: Union[str, Path], /,
                 *, submission_only: bool = False):
        """Run State-Sequence Grader."""
        # ref: stackoverflow.com/a/56764010
        calling_from_file_path: Path = Path(stack()[1].filename)

        with change_directory(calling_from_file_path.parent):
            with open(file=self._SUBMISSION_MODULE_FILE_NAME,
                      mode='wt', encoding='utf-8') as s:
                s.write(
                    f'print({self.output_comp_func(student_submission_file_path)})')   # noqa: E501

            if submission_only:
                pprint(run(grader_name=calling_from_file_path.stem,
                           submission_name=self._SUBMISSION_MODULE_NAME),
                       stream=None,
                       indent=2,
                       width=80,
                       depth=None,
                       compact=False,
                       sort_dicts=False,
                       # underscore_numbers=True   # Py3.10+
                       )

            else:
                main(args=(calling_from_file_path.name,
                           self._SUBMISSION_MODULE_FILE_NAME))

            os.remove(path=self._SUBMISSION_MODULE_FILE_NAME)
