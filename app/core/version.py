from subprocess import getoutput

from .environment import SHOW_COMMIT, VERSION


def get_version() -> str:
    """returns the current version "`v.<num>.<num>.<num>-<last_commit>`" """
    if SHOW_COMMIT:
        return f"v.{VERSION}-{getoutput('git describe --tags --always')}"
    else:
        return f"v.{VERSION}"
