"""State-Sequence Grader."""


from collections.abc import Callable
from inspect import stack
import os
from pathlib import Path
from pprint import pprint
from shutil import copyfile
from tempfile import NamedTemporaryFile
from typing import Optional, Union

from grader_support.gradelib import Grader
from grader_support.graderutil import change_directory
from grader_support.run import run

from xqueue_watcher.jailedgrader import main


OUTPUT_COMP_FUNC_TYPE: type = Callable[[Union[str, Path]], bool]


class StateSeqGrader(Grader):
    """State-Sequence Grader."""

    _SUBMISSION_MODULE_NAME: str = '_submission'
    _SUBMISSION_MODULE_FILE_NAME: str = f'{_SUBMISSION_MODULE_NAME}.py'

    def __init__(self, student_submission_file_test_func: OUTPUT_COMP_FUNC_TYPE, /):   # noqa: E501
        """Initialize State-Sequence Grader."""
        super().__init__()

        self.student_submission_file_test_func: OUTPUT_COMP_FUNC_TYPE = \
            student_submission_file_test_func

        self.add_input_check(check=self.check_student_submission_str)
        self.set_only_check_input(value=True)

    def check_student_submission_str(self, student_submission_str: str, /) -> bool:   # noqa: E501
        """Test student submission string."""
        with NamedTemporaryFile(mode='wt',
                                buffering=-1,
                                encoding='utf-8',
                                newline=None,
                                suffix=None,
                                prefix=None,
                                dir=None,
                                delete=False,
                                errors='strict') as f:
            f.write(student_submission_str)

        try:
            if self.student_submission_file_test_func(f.name):
                complaint_str: Optional[str] = None
            else:
                complaint_str: Optional[str] = '*** INCORRECT ***'

        except Exception as err:   # pylint: disable=broad-except
            complaint_str: Optional[str] = str(err)

        finally:
            os.remove(path=f.name)

        return complaint_str

    def __call__(self,
                 student_submission_file_path: Union[str, Path], /,
                 *, submission_only: bool = False):
        """Run State-Sequence Grader."""
        # ref: stackoverflow.com/a/56764010
        calling_from_file_path: Path = Path(stack()[1].filename)

        with change_directory(calling_from_file_path.parent):
            copyfile(src=student_submission_file_path,
                     dst=self._SUBMISSION_MODULE_FILE_NAME,
                     follow_symlinks=True)

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
