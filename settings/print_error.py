from enum import Enum
from github_action_utils import group, notice, error, echo

class BuildStatus(Enum):
    SUCCESS = 0
    FAILED = 1

class PrintError:
    build_status = BuildStatus.SUCCESS


class PrintSimpleError(PrintError):
    @staticmethod
    def print_error(errors, group_name=None):
        build_status = BuildStatus.FAILED
        if group_name is None:
            for e in errors:
                error(e)
        else:
            with group(group_name):
                for e in errors:
                    error(e)
        
            

class PrintErrorsWithLines(PrintError):
    @staticmethod
    def print_error(errors, lines, group_name=None):
        build_status = BuildStatus.FAILED
        if group_name is None:
            for e in errors:
                error(e)
                for line in lines:
                    echo('line: ' + str(line))
        else:
            with group(group_name):
                for e in errors:
                    error(e)
                    for line in lines:
                        echo('line: ' + str(line))