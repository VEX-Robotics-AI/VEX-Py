"""State-Sequence Grader."""


from ast import (Name, Load, Store,
                 Assign, Call, Constant, Lambda, Module,
                 fix_missing_locations, parse, unparse)
from collections.abc import Callable
from copy import copy
from inspect import stack
import os
from pathlib import Path
from pprint import pprint
from shutil import copyfile
from sys import executable
from tempfile import NamedTemporaryFile
from typing import Optional, Union

from grader_support.gradelib import Grader
from grader_support.graderutil import change_directory
from grader_support.run import run

from codejail.jail_code import configure

configure(command='python', bin_path=executable, user=None)

# pylint: disable=wrong-import-position
from codejail.safe_exec import SafeExecException, safe_exec   # noqa: E402


class StateSeqGrader(Grader):
    """State-Sequence Grader."""

    __full_qual_name__: str = f'{__name__}.{__qualname__}'

    _GRADER_VAR_NAME: str = 'grader'

    _SUBMISSION_FILE_TEST_FUNC_VAR_NAME: str = 'SUBMISSION_FILE_TEST_FUNC'
    _SUBMISSION_FILE_TEST_RESULT_VAR_NAME: str = \
        f'{_SUBMISSION_FILE_TEST_FUNC_VAR_NAME}_RESULT'

    _SUBMISSION_MODULE_NAME: str = '_submission'
    _SUBMISSION_MODULE_FILE_NAME: str = f'{_SUBMISSION_MODULE_NAME}.py'

    def __init__(self,
                 _unsafe_submission_file_test_func:
                 Callable[[Union[str, Path]], bool], /):
        """Initialize State-Sequence Grader."""
        super().__init__()

        self.add_input_check(check=self.check_submission_str)

        if hasattr(self, 'set_only_check_input'):   # S4V customization
            self.set_only_check_input(value=True)

        # stackoverflow.com/a/56764010
        self.file_path: Path = Path(stack()[1].filename)

        with open(file=self.file_path,
                  mode='rt',
                  buffering=-1,
                  encoding='utf-8',
                  errors='strict',
                  newline=None,
                  closefd=True,
                  opener=None) as f:
            self.module: Module = parse(source=f.read(),
                                        filename=self.file_path,
                                        mode='exec',
                                        type_comments=False,
                                        feature_version=None)

            # REQUIRED assignment to variable named `grader`
            grader_assignment: Assign = self.module.body.pop(
                next(i for i, node in enumerate(self.module.body)
                     if isinstance(node, Assign) and
                     node.targets[0].id == self._GRADER_VAR_NAME))

            # REQUIRED instantiation of StateSeqGrader class instance
            # with 1 single lambda positional argument
            assert isinstance(submission_file_test_func_code :=
                              grader_assignment.value.args[0], Lambda), \
                '*** SUBMISSION FILE TESTING FUNCTION MUST BE A LAMBDA ***'

            self.module.body.append(
                Assign(targets=[Name(id=self._SUBMISSION_FILE_TEST_FUNC_VAR_NAME,   # noqa: E501
                                     ctx=Store())],
                       value=submission_file_test_func_code,
                       type_comment=None))

    def check_submission_str(self, submission_str: str, /) -> Optional[str]:
        """Test submission string."""
        with NamedTemporaryFile(mode='wt',
                                buffering=-1,
                                encoding='utf-8',
                                newline=None,
                                suffix=None,
                                prefix=None,
                                dir=None,
                                delete=False,
                                errors='strict') as f:
            f.write(submission_str)

        (_module := copy(self.module)).body.append(
            Assign(targets=[Name(id=self._SUBMISSION_FILE_TEST_RESULT_VAR_NAME,
                                 ctx=Store())],
                   value=Call(func=Name(id=self._SUBMISSION_FILE_TEST_FUNC_VAR_NAME,   # noqa: E501
                                        ctx=Load()),
                              args=[Constant(value=f.name)],
                              keywords=[],
                              starargs=[],
                              kwargs=[]),
                   type_comment=None))

        try:
            safe_exec(code=(unparse(ast_obj=fix_missing_locations(node=_module))   # noqa: E501
                            .replace('__file__', f"'{self.file_path}'")),
                      globals_dict=(_globals := {}),
                      files=None,
                      python_path=None,
                      limit_overrides_context=None,
                      slug=self.__full_qual_name__,
                      extra_files=None)

            return (None
                    if _globals[self._SUBMISSION_FILE_TEST_RESULT_VAR_NAME]
                    else '*** INCORRECT ***')

        except SafeExecException as err:
            return (('*** SUBMISSION TAKES TOO LONG TO RUN '
                     '(LIKELY INFINITE LOOP) ***')
                    if (complaint_str := str(err)) in (
                        "Couldn't execute jailed code: "   # Linux
                        "stdout: b'', stderr: b'' with status code: -9",
                        "Couldn't execute jailed code: "   # MacOS
                        "stdout: b'', stderr: b'' with status code: -24",
                        )   # noqa: E123
                    else complaint_str)

        finally:
            os.remove(path=f.name)

    def __call__(self, submission_file_path: Union[str, Path], /,
                 *, submission_only: bool = False):
        """Run State-Sequence Grader."""
        with change_directory(self.file_path.parent):
            # pylint: disable=import-outside-toplevel
            if submission_only:
                copyfile(src=submission_file_path,
                         dst=self._SUBMISSION_MODULE_FILE_NAME,
                         follow_symlinks=True)

                pprint(run(grader_name=self.file_path.stem,
                           submission_name=self._SUBMISSION_MODULE_NAME),
                       stream=None,
                       indent=2,
                       width=80,
                       depth=None,
                       compact=False,
                       sort_dicts=False,
                       underscore_numbers=True)

                os.remove(path=self._SUBMISSION_MODULE_FILE_NAME)

            else:
                from xqueue_watcher.jailedgrader import main

                main(args=(self.file_path.name, submission_file_path))
