from typing import Optional

from django import get_version


# TODO: Be able to return more than just the major version, but as an int.
def get_django_version() -> int:
    """ Returns the major version number of Django as an int. """
    major, minor, patch = [ int(x, 10) for x in get_version().split('.') ]
    if major > 0:
        return major
    else:
        # TODO: Literally anything other than a basic Exception.
        raise Exception
