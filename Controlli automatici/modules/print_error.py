from enum import Enum
from github_action_utils import group, notice, error, echo, warning

class BuildStatus(Enum):
    SUCCESS = 0
    FAILED = 1

class PrintError:
    build_status = BuildStatus.SUCCESS


class PrintSimpleError(PrintError):
    @staticmethod
    def print_error(errors, group_name=None):
        PrintError.build_status = BuildStatus.FAILED
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
        PrintError.build_status = BuildStatus.FAILED
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


class PrintWarning(PrintError):
    @staticmethod
    def print_warning(warnings, group_name=None):
        if group_name is None:
            for w in warnings:
                warning(w)
        else:
            with group(group_name):
                for w in warnings:
                    warning(w)