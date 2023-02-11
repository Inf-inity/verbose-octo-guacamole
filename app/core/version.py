from subprocess import getoutput

from .environment import SHOW_COMMIT, VERSION


def get_version() -> str:
    """returns the current version "`v.<major>.<minor>.<patch>-<last_commit>@<current_branch>`" """
    if SHOW_COMMIT:
        return f"v.{VERSION}-{getoutput('git describe --tags --always')}@{getoutput('git branch --show-current')}"
    else:
        return f"v.{VERSION}"
