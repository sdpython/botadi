"""
@file
@brief Exception for Mokadi.
"""


class MokadiException(Exception):
    """
    Mokadi exception.
    """
    pass  # pylint: disable=W0107


class CognitiveException(Exception):
    """
    Failure when calling the API.
    """
    pass  # pylint: disable=W0107


class WikipediaException(Exception):
    """
    Issue with :epkg:`wikipedia`.
    """
    pass  # pylint: disable=W0107


class MokadiAuthentification(Exception):
    """
    Issue with authentification.
    """
    pass  # pylint: disable=W0107
